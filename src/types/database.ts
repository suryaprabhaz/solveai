export interface SearchFilter {
  language?: string;
  subject?: string;
  topic?: string;
  difficulty?: string;
  limit?: number;
}

export interface SearchResult {
  id: string;
  title: string;
  question: string;
  language: string;
  subject: string;
  topic: string;
  subtopic?: string;
  difficulty: string;
  tags?: string;
  code: string;
  explanation?: string;
  timeComplexity?: string;
  spaceComplexity?: string;
  sampleInput?: string;
  sampleOutput?: string;
  score?: number;
  source: 'database_exact' | 'database_fts' | 'database_keyword' | 'ollama';
}

export interface DatabaseStats {
  totalQuestions: number;
  totalSolutions: number;
  languages: { [lang: string]: number };
  subjects: { [subject: string]: number };
}
