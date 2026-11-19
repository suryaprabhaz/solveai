import * as vscode from 'vscode';

export async function showAnswerPreview(
  answer: string,
  model: string
): Promise<'apply' | 'copy' | 'cancel'> {
  const truncated = answer.length > 300 ? answer.substring(0, 300) + '\n…(truncated in preview)' : answer;

  const choice = await vscode.window.showInformationMessage(
    `SolveAI answer ready (${model}):\n\n${truncated}`,
    { modal: true },
    'Apply to Editor',
    'Copy to Clipboard'
  );

  if (choice === 'Apply to Editor') {
    return 'apply';
  }
  if (choice === 'Copy to Clipboard') {
    return 'copy';
  }
  return 'cancel';
}

export async function showExplanationPanel(
  explanation: string,
  language: string
): Promise<void> {
  const panel = vscode.window.createWebviewPanel(
    'solveaiExplain',
    `SolveAI: Explanation (${language})`,
    vscode.ViewColumn.Beside,
    { enableScripts: false }
  );

  panel.webview.html = buildExplanationHtml(explanation, language);
}

function buildExplanationHtml(explanation: string, language: string): string {
  const escaped = explanation
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>');

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SolveAI Explanation</title>
<style>
  body {
    font-family: var(--vscode-font-family);
    font-size: var(--vscode-font-size);
    color: var(--vscode-foreground);
    background: var(--vscode-editor-background);
    padding: 16px 24px;
    line-height: 1.6;
  }
  h2 {
    font-size: 1.1em;
    color: var(--vscode-textLink-foreground);
    margin-bottom: 12px;
    border-bottom: 1px solid var(--vscode-panel-border);
    padding-bottom: 8px;
  }
  .content {
    white-space: pre-wrap;
    word-break: break-word;
  }
</style>
</head>
<body>
<h2>SolveAI Explanation — ${language}</h2>
<div class="content">${escaped}</div>
</body>
</html>`;
}
