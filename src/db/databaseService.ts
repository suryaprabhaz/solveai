import * as fs from 'fs';
import * as path from 'path';
import { SearchFilter, SearchResult, DatabaseStats } from '../types/database';

export interface CatalogItem {
  id: string;
  title: string;
  language: string;
  subject: string;
  topic: string;
  subtopic?: string;
  difficulty: string;
  tags: string[];
  normalized_question: string;
  time_complexity?: string;
  space_complexity?: string;
  code: string;
  explanation?: string;
}

export class DatabaseService {
  private items: CatalogItem[] = [];
  private isLoaded: boolean = false;
  private dbPath: string = '';

  constructor() {
    this.loadCatalog();
  }

  private loadCatalog(): void {
    if (this.isLoaded) return;
    try {
      // 1. Try resolving relative to package root / out folder
      const candidatePaths = [
        path.join(__dirname, '../../data/catalog.json'),
        path.join(__dirname, '../data/catalog.json'),
        path.join(__dirname, 'data/catalog.json'),
        path.resolve('data/catalog.json')
      ];

      for (const p of candidatePaths) {
        if (fs.existsSync(p)) {
          const raw = fs.readFileSync(p, 'utf-8');
          this.items = JSON.parse(raw);
          this.dbPath = p;
          this.isLoaded = true;
          break;
        }
      }
    } catch (e) {
      this.items = [];
    }
  }

  public getAll(): CatalogItem[] {
    this.loadCatalog();
    return this.items;
  }

  public getStats(): DatabaseStats {
    this.loadCatalog();
    const stats: DatabaseStats = {
      totalQuestions: this.items.length,
      totalSolutions: this.items.length,
      languages: {},
      subjects: {}
    };

    for (const item of this.items) {
      const l = item.language.toLowerCase();
      const s = item.subject;
      stats.languages[l] = (stats.languages[l] || 0) + 1;
      stats.subjects[s] = (stats.subjects[s] || 0) + 1;
    }

    return stats;
  }

  public search(query: string, filter?: SearchFilter): SearchResult[] {
    this.loadCatalog();
    const rawQ = query.toLowerCase().trim();
    if (!rawQ) return [];

    const normQ = rawQ.replace(/[\r\n\t]+/g, ' ').replace(/[^\w\s,\.\-\+\#]/g, ' ').replace(/\s+/g, ' ').trim();
    const targetLang = filter?.language ? filter.language.toLowerCase().trim() : undefined;
    const targetSubject = filter?.subject ? filter.subject.toLowerCase().trim() : undefined;
    const targetTopic = filter?.topic ? filter.topic.toLowerCase().trim() : undefined;
    const limit = filter?.limit || 10;

    const scored: { item: CatalogItem; score: number; source: SearchResult['source'] }[] = [];

    const queryTokens = normQ.split(' ').filter(t => t.length > 1);

    for (const item of this.items) {
      // Language filter
      if (targetLang && item.language.toLowerCase() !== targetLang) {
        continue;
      }
      // Subject filter
      if (targetSubject && !item.subject.toLowerCase().includes(targetSubject)) {
        continue;
      }
      // Topic filter
      if (targetTopic && !item.topic.toLowerCase().includes(targetTopic)) {
        continue;
      }

      const itemTitleNorm = item.title.toLowerCase();
      const itemNormQ = (item.normalized_question || '').toLowerCase();
      const itemTags = (item.tags || []).join(' ').toLowerCase();

      let score = 0;
      let matchSource: SearchResult['source'] = 'database_keyword';

      // Exact title match
      if (itemTitleNorm === normQ || itemTitleNorm.includes(normQ)) {
        score += 100;
        matchSource = 'database_exact';
      }

      // Keyword / shorthand match (e.g. "bar plot,py" or "binary search")
      for (const tag of item.tags) {
        const tagNorm = tag.toLowerCase();
        if (normQ.includes(tagNorm)) {
          score += 30 + tagNorm.length;
        }
      }

      // Token overlap
      let tokenMatches = 0;
      for (const token of queryTokens) {
        if (itemTitleNorm.includes(token)) {
          score += 15;
          tokenMatches++;
        } else if (itemNormQ.includes(token)) {
          score += 10;
          tokenMatches++;
        } else if (itemTags.includes(token)) {
          score += 5;
          tokenMatches++;
        }
      }

      if (score > 0) {
        scored.push({ item, score, source: matchSource });
      }
    }

    scored.sort((a, b) => b.score - a.score);

    return scored.slice(0, limit).map(s => ({
      id: s.item.id,
      title: s.item.title,
      question: s.item.title,
      language: s.item.language,
      subject: s.item.subject,
      topic: s.item.topic,
      subtopic: s.item.subtopic,
      difficulty: s.item.difficulty,
      tags: s.item.tags.join(', '),
      code: s.item.code,
      explanation: s.item.explanation,
      timeComplexity: s.item.time_complexity,
      spaceComplexity: s.item.space_complexity,
      score: s.score,
      source: s.source
    }));
  }
}

export const databaseService = new DatabaseService();
