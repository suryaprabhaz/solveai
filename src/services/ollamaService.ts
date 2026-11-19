import * as vscode from 'vscode';
import { OllamaConfig, OllamaRequest, OllamaResponse, OllamaTagsResponse, SolveResult } from '../types';

export class OllamaService {
  private getConfig(): OllamaConfig {
    const cfg = vscode.workspace.getConfiguration('solveai.ollama');
    return {
      baseUrl: cfg.get<string>('baseUrl', 'http://localhost:11434').replace(/\/$/, ''),
      model: cfg.get<string>('model', 'qwen3:8b'),
      timeout: cfg.get<number>('timeout', 120000),
      apiKey: cfg.get<string>('apiKey', ''),
      autoApply: cfg.get<boolean>('autoApply', false),
    };
  }

  private buildHeaders(apiKey: string): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };
    if (apiKey && apiKey.trim().length > 0) {
      headers['Authorization'] = `Bearer ${apiKey}`;
    }
    return headers;
  }

  async listModels(): Promise<string[]> {
    const cfg = this.getConfig();
    const url = `${cfg.baseUrl}/api/tags`;

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), Math.min(cfg.timeout, 10000));

    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: this.buildHeaders(cfg.apiKey),
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = (await response.json()) as OllamaTagsResponse;
      return (data.models ?? []).map((m) => m.name);
    } finally {
      clearTimeout(timer);
    }
  }

  async checkConnection(): Promise<{ connected: boolean; models: string[]; error?: string }> {
    try {
      const models = await this.listModels();
      return { connected: true, models };
    } catch (error) {
      const msg = error instanceof Error ? error.message : String(error);
      return { connected: false, models: [], error: msg };
    }
  }

  async sendPrompt(prompt: string): Promise<SolveResult> {
    const cfg = this.getConfig();
    const url = `${cfg.baseUrl}/api/chat`;

    const requestBody: OllamaRequest = {
      model: cfg.model,
      messages: [{ role: 'user', content: prompt }],
      stream: false,
    };

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), cfg.timeout);

    const startTime = Date.now();

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: this.buildHeaders(cfg.apiKey),
        body: JSON.stringify(requestBody),
        signal: controller.signal,
      });

      if (!response.ok) {
        const bodyText = await response.text().catch(() => '');
        if (response.status === 404 && bodyText.toLowerCase().includes('model')) {
          throw new Error(
            `Model "${cfg.model}" not found in Ollama.\n\nRun: ollama pull ${cfg.model}`
          );
        }
        throw new Error(`HTTP ${response.status}: ${response.statusText}. ${bodyText}`);
      }

      const data = (await response.json()) as OllamaResponse;

      if (!data.message?.content) {
        throw new Error('Empty response received from Ollama.');
      }

      return {
        answer: data.message.content,
        model: data.model ?? cfg.model,
        durationMs: Date.now() - startTime,
      };
    } catch (error) {
      if (error instanceof Error && error.name === 'AbortError') {
        throw new Error(
          `Request timed out after ${cfg.timeout / 1000}s.\n\nTry increasing solveai.ollama.timeout or use a faster/smaller model.`
        );
      }
      throw error;
    } finally {
      clearTimeout(timer);
    }
  }

  getModel(): string {
    return this.getConfig().model;
  }

  getBaseUrl(): string {
    return this.getConfig().baseUrl;
  }

  isAutoApply(): boolean {
    return this.getConfig().autoApply;
  }
}

export const ollamaService = new OllamaService();
