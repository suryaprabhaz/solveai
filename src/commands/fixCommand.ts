import * as vscode from 'vscode';
import { ollamaService } from '../services/ollamaService';
import { buildFixPrompt, stripCodeFences } from '../services/promptService';
import { getActiveEditorContext, validateInputSize, applyAnswerToEditor } from '../utils/editorUtils';
import { buildConnectionErrorMessage } from '../utils/errorUtils';
import { shouldStripCodeFences } from '../utils/languageUtils';
import { showAnswerPreview } from '../ui/previewPanel';
import { StatusBarManager } from '../ui/statusBar';

export async function fixCommand(statusBar: StatusBarManager): Promise<void> {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showWarningMessage('SolveAI: No active editor. Open a file first.');
    return;
  }

  const context = getActiveEditorContext();
  if (!context || context.text.trim().length === 0) {
    vscode.window.showWarningMessage('SolveAI: Select the code you want to fix.');
    return;
  }

  const validation = validateInputSize(context.text);
  if (!validation.valid) {
    vscode.window.showWarningMessage(`SolveAI: ${validation.message}`);
    return;
  }

  statusBar.setWorking();

  try {
    const prompt = buildFixPrompt(context);
    const result = await ollamaService.sendPrompt(prompt);

    const strip = shouldStripCodeFences(editor.document.languageId);
    const cleanAnswer = stripCodeFences(result.answer, strip);

    if (ollamaService.isAutoApply()) {
      await applyAnswerToEditor(editor, cleanAnswer, context);
      vscode.window.showInformationMessage(`SolveAI: Fixed code applied from ${result.model}.`);
    } else {
      const choice = await showAnswerPreview(cleanAnswer, result.model);
      if (choice === 'apply') {
        await applyAnswerToEditor(editor, cleanAnswer, context);
        vscode.window.showInformationMessage('SolveAI: Fixed code applied to editor.');
      } else if (choice === 'copy') {
        await vscode.env.clipboard.writeText(cleanAnswer);
        vscode.window.showInformationMessage('SolveAI: Fixed code copied to clipboard.');
      }
    }
  } catch (error) {
    const baseUrl = ollamaService.getBaseUrl();
    const msg = buildConnectionErrorMessage(baseUrl, error);
    vscode.window.showErrorMessage(msg);
  } finally {
    statusBar.setReady();
  }
}
