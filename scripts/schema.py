import sqlite3
import json
import os
import sys

SCHEMA_SQL = """
-- Core questions table
CREATE TABLE IF NOT EXISTS questions (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    question TEXT NOT NULL,
    normalized_question TEXT NOT NULL,
    description TEXT,
    language TEXT NOT NULL,
    subject TEXT NOT NULL,
    topic TEXT NOT NULL,
    subtopic TEXT,
    difficulty TEXT NOT NULL,
    tags TEXT,
    input_format TEXT,
    output_format TEXT,
    constraints TEXT,
    sample_input TEXT,
    sample_output TEXT,
    explanation TEXT,
    time_complexity TEXT,
    space_complexity TEXT,
    source_type TEXT DEFAULT 'curriculum',
    verified INTEGER DEFAULT 1,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Core solutions table
CREATE TABLE IF NOT EXISTS solutions (
    id TEXT PRIMARY KEY,
    question_id TEXT NOT NULL,
    language TEXT NOT NULL,
    code TEXT NOT NULL,
    explanation TEXT,
    algorithm TEXT,
    time_complexity TEXT,
    space_complexity TEXT,
    tested INTEGER DEFAULT 1,
    test_cases TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Test cases table
CREATE TABLE IF NOT EXISTS test_cases (
    id TEXT PRIMARY KEY,
    solution_id TEXT NOT NULL,
    input TEXT,
    expected_output TEXT,
    FOREIGN KEY(solution_id) REFERENCES solutions(id) ON DELETE CASCADE
);

-- Tags table
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

-- Question-Tag relationship
CREATE TABLE IF NOT EXISTS question_tags (
    question_id TEXT NOT NULL,
    tag_name TEXT NOT NULL,
    PRIMARY KEY (question_id, tag_name),
    FOREIGN KEY(question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Full-Text Search (FTS5) for instant keyword & semantic ranking
CREATE VIRTUAL TABLE IF NOT EXISTS questions_fts USING fts5(
    id UNINDEXED,
    title,
    normalized_question,
    tags,
    language,
    subject,
    topic,
    tokenize = 'unicode61 remove_diacritics 1'
);

-- Indexes for lightning-fast exact and filtered queries
CREATE INDEX IF NOT EXISTS idx_questions_lang ON questions(language);
CREATE INDEX IF NOT EXISTS idx_questions_subject ON questions(subject);
CREATE INDEX IF NOT EXISTS idx_questions_topic ON questions(topic);
CREATE INDEX IF NOT EXISTS idx_questions_difficulty ON questions(difficulty);
CREATE INDEX IF NOT EXISTS idx_questions_norm ON questions(normalized_question);
CREATE INDEX IF NOT EXISTS idx_solutions_qid ON solutions(question_id);
"""

def init_db(db_path):
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA_SQL)
    con.commit()
    return con

if __name__ == '__main__':
    db_file = sys.argv[1] if len(sys.argv) > 1 else 'data/solveai.db'
    con = init_db(db_file)
    print(f"Database schema initialized successfully at {db_file}")
    con.close()
