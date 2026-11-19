import * as vscode from 'vscode';
import { ConnectionStatus, ConnectionInfo } from '../types';
import { ollamaService } from './ollamaService';

export class ConnectionService {
  private _status: ConnectionStatus = 'offline';
  private _lastCheck: Date | undefined;

  get status(): ConnectionStatus {
    return this._status;
  }

  async check(): Promise<ConnectionInfo> {
    const result = await ollamaService.checkConnection();
    this._lastCheck = new Date();

    if (result.connected) {
      this._status = 'connected';
      const model = ollamaService.getModel();
      return { status: 'connected', model };
    } else {
      this._status = 'offline';
      return { status: 'offline', error: result.error };
    }
  }

  getStatusIcon(): string {
    switch (this._status) {
      case 'connected': return '$(sparkle) Solve';
      case 'error': return '$(warning) Solve';
      default: return '$(sparkle) Solve';
    }
  }
}

export const connectionService = new ConnectionService();
