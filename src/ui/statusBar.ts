import * as vscode from 'vscode';

export class StatusBarManager {
  private item: vscode.StatusBarItem;

  constructor() {
    this.item = vscode.window.createStatusBarItem(
      vscode.StatusBarAlignment.Right,
      100
    );
    this.item.command = 'solveai.solve';
    this.item.text = '$(sparkle) Solve';
    this.item.tooltip = 'SolveAI: Solve coding question with local AI (Ctrl+Alt+S)';
    this.item.name = 'SolveAI';
  }

  show(): void {
    this.item.show();
  }

  hide(): void {
    this.item.hide();
  }

  setWorking(): void {
    this.item.text = '$(loading~spin) Solving…';
    this.item.tooltip = 'SolveAI: Generating answer…';
    this.item.command = undefined;
  }

  setReady(): void {
    this.item.text = '$(sparkle) Solve';
    this.item.tooltip = 'SolveAI: Solve coding question with local AI (Ctrl+Alt+S)';
    this.item.command = 'solveai.solve';
  }

  setError(): void {
    this.item.text = '$(warning) Solve';
    this.item.tooltip = 'SolveAI: AI unavailable — click to retry';
    this.item.command = 'solveai.checkConnection';
  }

  dispose(): void {
    this.item.dispose();
  }
}
