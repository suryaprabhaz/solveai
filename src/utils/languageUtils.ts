const LANGUAGE_DISPLAY_NAMES: Record<string, string> = {
  python: 'Python',
  r: 'R',
  java: 'Java',
  c: 'C',
  cpp: 'C++',
  javascript: 'JavaScript',
  typescript: 'TypeScript',
  html: 'HTML',
  css: 'CSS',
  sql: 'SQL',
  shellscript: 'Shell',
  bash: 'Bash',
  go: 'Go',
  rust: 'Rust',
  php: 'PHP',
  ruby: 'Ruby',
  csharp: 'C#',
  kotlin: 'Kotlin',
  swift: 'Swift',
  markdown: 'Markdown',
  json: 'JSON',
  xml: 'XML',
  yaml: 'YAML',
};

const EXTENSION_TO_LANGUAGE: Record<string, string> = {
  '.py': 'Python',
  '.r': 'R',
  '.R': 'R',
  '.java': 'Java',
  '.c': 'C',
  '.cpp': 'C++',
  '.cc': 'C++',
  '.cxx': 'C++',
  '.js': 'JavaScript',
  '.ts': 'TypeScript',
  '.html': 'HTML',
  '.htm': 'HTML',
  '.css': 'CSS',
  '.sql': 'SQL',
  '.sh': 'Shell',
  '.go': 'Go',
  '.rs': 'Rust',
  '.php': 'PHP',
  '.rb': 'Ruby',
  '.cs': 'C#',
  '.kt': 'Kotlin',
  '.swift': 'Swift',
};

export function getLanguageDisplayName(languageId: string): string {
  return LANGUAGE_DISPLAY_NAMES[languageId.toLowerCase()] ?? languageId;
}

export function getLanguageFromExtension(filePath: string): string | undefined {
  const ext = filePath.substring(filePath.lastIndexOf('.'));
  return EXTENSION_TO_LANGUAGE[ext];
}

export function isMarkdownDocument(languageId: string): boolean {
  return languageId === 'markdown';
}

export function shouldStripCodeFences(languageId: string): boolean {
  return !isMarkdownDocument(languageId);
}
