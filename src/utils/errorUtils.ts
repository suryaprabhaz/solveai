export function formatError(error: unknown): string {
  if (error instanceof Error) {
    return error.message;
  }
  if (typeof error === 'string') {
    return error;
  }
  return 'An unknown error occurred.';
}

export function isNetworkError(error: unknown): boolean {
  if (error instanceof Error) {
    const msg = error.message.toLowerCase();
    return (
      msg.includes('econnrefused') ||
      msg.includes('enotfound') ||
      msg.includes('network') ||
      msg.includes('fetch') ||
      msg.includes('timeout') ||
      msg.includes('abort')
    );
  }
  return false;
}

export function buildConnectionErrorMessage(baseUrl: string, error: unknown): string {
  const details = formatError(error);
  return [
    'Cannot connect to Ollama.',
    '',
    'Check:',
    '  • Ollama is running on your laptop',
    `  • Server URL is correct: ${baseUrl}`,
    '  • Your laptop and this computer can communicate (same network)',
    '  • The selected model is installed in Ollama',
    '',
    `Detail: ${details}`,
  ].join('\n');
}
