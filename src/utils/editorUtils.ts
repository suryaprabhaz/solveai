import type * as vscodeTypes from 'vscode';
import { EditorContext } from '../types';
import { getLanguageDisplayName } from './languageUtils';

const MAX_INPUT_CHARS = 8000;

export function getActiveEditorContext(): EditorContext | undefined {
  // Dynamically require vscode so non-extension environments (e.g. CLI mocha tests) don't crash on import
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const vscode = require('vscode') as typeof import('vscode');
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    return undefined;
  }

  const document = editor.document;
  const selection = editor.selection;
  const languageId = document.languageId;
  const language = getLanguageDisplayName(languageId);

  if (!selection.isEmpty) {
    const text = document.getText(selection);
    return { text, language, isSelection: true, selection, document };
  }

  // Try current line
  const currentLine = document.lineAt(selection.active.line);
  const lineText = currentLine.text.trim();
  if (lineText.length > 10) {
    // Try to get surrounding block (up to 20 lines)
    const startLine = Math.max(0, selection.active.line - 2);
    const endLine = Math.min(document.lineCount - 1, selection.active.line + 17);
    const range = new vscode.Range(startLine, 0, endLine, document.lineAt(endLine).text.length);
    const blockText = document.getText(range).trim();
    if (blockText.length > 0) {
      return { text: blockText, language, isSelection: false, selection, document };
    }
  }

  // Fall back to entire document
  const fullText = document.getText().trim();
  return { text: fullText, language, isSelection: false, selection, document };
}

export function validateInputSize(text: string): { valid: boolean; message?: string } {
  if (text.length > MAX_INPUT_CHARS) {
    return {
      valid: false,
      message: `The selected content is too large for SolveAI (${text.length} chars, max ${MAX_INPUT_CHARS}).\n\nSelect only the question/code you want to solve.`,
    };
  }
  if (text.trim().length === 0) {
    return { valid: false, message: 'No text found. Please type or select a question first.' };
  }
  return { valid: true };
}

export async function applyAnswerToEditor(
  editor: vscodeTypes.TextEditor,
  answer: string,
  context: EditorContext
): Promise<boolean> {
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const vscode = require('vscode') as typeof import('vscode');
  return editor.edit((editBuilder) => {
    if (context.isSelection && context.selection) {
      editBuilder.replace(context.selection, answer);
    } else {
      const fullRange = new vscode.Range(
        0, 0,
        editor.document.lineCount - 1,
        editor.document.lineAt(editor.document.lineCount - 1).text.length
      );
      editBuilder.replace(fullRange, answer);
    }
  });
}

