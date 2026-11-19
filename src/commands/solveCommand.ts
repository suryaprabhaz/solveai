import * as vscode from 'vscode';
import { ollamaService } from '../services/ollamaService';
import { buildSolvePrompt, stripCodeFences } from '../services/promptService';
import { findOfflineMatch } from '../services/offlineDatabase';
import { getActiveEditorContext, validateInputSize, applyAnswerToEditor } from '../utils/editorUtils';
import { buildConnectionErrorMessage } from '../utils/errorUtils';
import { shouldStripCodeFences } from '../utils/languageUtils';
import { showAnswerPreview } from '../ui/previewPanel';
import { StatusBarManager } from '../ui/statusBar';

export async function solveCommand(statusBar: StatusBarManager): Promise<void> {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showWarningMessage('SolveAI: No active editor. Open a file first.');
    return;
  }

  let context = getActiveEditorContext();

  if (!context || context.text.trim().length === 0) {
    // Show input dialog
    const userInput = await vscode.window.showInputBox({
      prompt: 'What do you want to solve?',
      placeHolder: 'e.g. bar chart in python / histogram in r',
      ignoreFocusOut: true,
    });

    if (!userInput || userInput.trim().length === 0) {
      return;
    }

    const languageId = editor.document.languageId;
    const { getLanguageDisplayName } = await import('../utils/languageUtils');
    context = {
      text: userInput.trim(),
      language: getLanguageDisplayName(languageId),
      isSelection: false,
      document: editor.document,
    };
  }

  const validation = validateInputSize(context.text);
  if (!validation.valid) {
    vscode.window.showWarningMessage(`SolveAI: ${validation.message}`);
    return;
  }

  statusBar.setWorking();

  // 1. If user question matches the offline syllabus database, answer INSTANTLY (0 delay, no waiting on Ollama)
  const offlineMatch = findOfflineMatch(context.text, context.language);
  if (offlineMatch) {
    statusBar.setReady();
    await presentAnswer(editor, offlineMatch.code, `Offline Knowledge Base (${offlineMatch.title})`, context);
    return;
  }

  // 2. Otherwise send to Ollama LLM
  try {
    const prompt = buildSolvePrompt(context);
    const result = await ollamaService.sendPrompt(prompt);

    const strip = shouldStripCodeFences(editor.document.languageId);
    const cleanAnswer = stripCodeFences(result.answer, strip);

    await presentAnswer(editor, cleanAnswer, result.model, context);
  } catch (error) {
    const baseUrl = ollamaService.getBaseUrl();
    const msg = buildConnectionErrorMessage(baseUrl, error);
    vscode.window.showErrorMessage(msg);
  } finally {
    statusBar.setReady();
  }
}

async function presentAnswer(
  editor: vscode.TextEditor,
  answer: string,
  sourceModel: string,
  context: any
): Promise<void> {
  if (ollamaService.isAutoApply()) {
    await applyAnswerToEditor(editor, answer, context);
    vscode.window.showInformationMessage(`SolveAI: Applied answer from ${sourceModel}.`);
  } else {
    const choice = await showAnswerPreview(answer, sourceModel);
    if (choice === 'apply') {
      await applyAnswerToEditor(editor, answer, context);
      vscode.window.showInformationMessage('SolveAI: Answer applied to editor.');
    } else if (choice === 'copy') {
      await vscode.env.clipboard.writeText(answer);
      vscode.window.showInformationMessage('SolveAI: Answer copied to clipboard.');
    }
  }
}

