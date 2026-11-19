export interface OllamaConfig {
  baseUrl: string;
  model: string;
  timeout: number;
  apiKey: string;
  autoApply: boolean;
}

export interface OllamaMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export interface OllamaRequest {
  model: string;
  messages: OllamaMessage[];
  stream: boolean;
  options?: {
    temperature?: number;
    num_predict?: number;
  };
}

export interface OllamaResponse {
  model: string;
  created_at: string;
  message: OllamaMessage;
  done: boolean;
  total_duration?: number;
}

export interface OllamaModel {
  name: string;
  modified_at: string;
  size: number;
}

export interface OllamaTagsResponse {
  models: OllamaModel[];
}

export interface SolveResult {
  answer: string;
  model: string;
  durationMs?: number;
}

export type ConnectionStatus = 'connected' | 'offline' | 'error';

export interface ConnectionInfo {
  status: ConnectionStatus;
  model?: string;
  error?: string;
}

export interface EditorContext {
  text: string;
  language: string;
  isSelection: boolean;
  selection?: import('vscode').Selection;
  document?: import('vscode').TextDocument;
}
