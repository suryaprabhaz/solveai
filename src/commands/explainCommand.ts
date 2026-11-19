import * as vscode from 'vscode';
import { ollamaService } from '../services/ollamaService';
import { buildExplainPrompt } from '../services/promptService';
import { getActiveEditorContext, validateInputSize } from '../utils/editorUtils';
import { buildConnectionErrorMessage } from '../utils/errorUtils';
import { showExplanationPanel } from '../ui/previewPanel';
import { StatusBarManager } from '../ui/statusBar';

export async function explainCommand(statusBar: StatusBarManager): Promise<void> {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showWarningMessage('SolveAI: No active editor. Open a file first.');
    return;
  }

  const context = getActiveEditorContext();
  if (!context || context.text.trim().length === 0) {
    vscode.window.showWarningMessage('SolveAI: Select the code you want explained.');
    return;
  }

  const validation = validateInputSize(context.text);
  if (!validation.valid) {
    vscode.window.showWarningMessage(`SolveAI: ${validation.message}`);
    return;
  }

  statusBar.setWorking();

  try {
    const prompt = buildExplainPrompt(context);
    const result = await ollamaService.sendPrompt(prompt);

    await showExplanationPanel(result.answer, context.language);
  } catch (error) {
    const baseUrl = ollamaService.getBaseUrl();
    const msg = buildConnectionErrorMessage(baseUrl, error);
    vscode.window.showErrorMessage(msg);
  } finally {
    statusBar.setReady();
  }
}
