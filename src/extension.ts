import * as vscode from 'vscode';
import { StatusBarManager } from './ui/statusBar';
import { solveCommand } from './commands/solveCommand';
import { fixCommand } from './commands/fixCommand';
import { explainCommand } from './commands/explainCommand';
import { ollamaService } from './services/ollamaService';
import { buildConnectionErrorMessage } from './utils/errorUtils';

let statusBar: StatusBarManager;

export function activate(context: vscode.ExtensionContext): void {
  statusBar = new StatusBarManager();
  statusBar.show();

  context.subscriptions.push(
    statusBar as unknown as vscode.Disposable,

    vscode.commands.registerCommand('solveai.solve', async () => {
      await solveCommand(statusBar);
    }),

    vscode.commands.registerCommand('solveai.fix', async () => {
      await fixCommand(statusBar);
    }),

    vscode.commands.registerCommand('solveai.explain', async () => {
      await explainCommand(statusBar);
    }),

    vscode.commands.registerCommand('solveai.checkConnection', async () => {
      await checkConnectionCommand();
    }),

    vscode.commands.registerCommand('solveai.selectModel', async () => {
      await selectModelCommand();
    }),

    vscode.commands.registerCommand('solveai.openSettings', () => {
      vscode.commands.executeCommand(
        'workbench.action.openSettings',
        'solveai'
      );
    })
  );

  // Show connection status info on first activation (silent)
  ollamaService.checkConnection().then((result) => {
    if (!result.connected) {
      statusBar.setError();
      // Don't pop a notification — just update the status bar
    }
  }).catch(() => {
    statusBar.setError();
  });
}

async function checkConnectionCommand(): Promise<void> {
  const baseUrl = ollamaService.getBaseUrl();
  const model = ollamaService.getModel();

  await vscode.window.withProgress(
    {
      location: vscode.ProgressLocation.Notification,
      title: 'SolveAI: Checking connection…',
      cancellable: false,
    },
    async () => {
      const result = await ollamaService.checkConnection();

      if (result.connected) {
        const modelInstalled = result.models.includes(model);
        const modelStatus = modelInstalled
          ? `Model: ${model} ✓`
          : `Model: ${model} ✗ (not found — run: ollama pull ${model})`;

        vscode.window.showInformationMessage(
          `SolveAI connected successfully!\n\nServer: ${baseUrl}\n${modelStatus}\n\nAvailable models: ${result.models.join(', ') || 'none'}`
        );
        statusBar.setReady();
      } else {
        const msg = buildConnectionErrorMessage(baseUrl, result.error ?? 'Unknown error');
        vscode.window.showErrorMessage(msg);
        statusBar.setError();
      }
    }
  );
}

async function selectModelCommand(): Promise<void> {
  const currentModel = ollamaService.getModel();

  await vscode.window.withProgress(
    {
      location: vscode.ProgressLocation.Notification,
      title: 'SolveAI: Fetching models…',
      cancellable: false,
    },
    async (progress) => {
      let models: string[] = [];

      try {
        models = await ollamaService.listModels();
      } catch {
        vscode.window.showErrorMessage(
          'SolveAI: Could not reach Ollama to list models. Check your connection settings.'
        );
        return;
      }

      progress.report({ increment: 100 });

      if (models.length === 0) {
        vscode.window.showWarningMessage(
          'No Ollama models found.\n\nInstall a model first: ollama pull qwen3:8b'
        );
        return;
      }

      const items = models.map((m) => ({
        label: m,
        description: m === currentModel ? '(currently selected)' : '',
      }));

      const selected = await vscode.window.showQuickPick(items, {
        title: 'Select SolveAI Model',
        placeHolder: 'Choose the Ollama model to use',
      });

      if (selected) {
        await vscode.workspace
          .getConfiguration('solveai.ollama')
          .update('model', selected.label, vscode.ConfigurationTarget.Global);
        vscode.window.showInformationMessage(`SolveAI: Model set to ${selected.label}`);
      }
    }
  );
}

export function deactivate(): void {
  statusBar?.dispose();
}
