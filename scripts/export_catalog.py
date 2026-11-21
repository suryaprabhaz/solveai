import os
import json
import sqlite3

def export_offline_catalog(db_path, output_json, output_ts):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    cur.execute("""
        SELECT q.id, q.title, q.language, q.subject, q.topic, q.subtopic,
               q.difficulty, q.tags, q.normalized_question, q.time_complexity,
               q.space_complexity, s.code, s.explanation
        FROM questions q
        JOIN solutions s ON q.id = s.question_id
        ORDER BY q.language, q.title
    """)
    
    rows = cur.fetchall()
    catalog = []
    
    for r in rows:
        tags_list = [t.strip() for t in (r[7] or '').split(',') if t.strip()]
        catalog.append({
            "id": r[0],
            "title": r[1],
            "language": r[2],
            "subject": r[3],
            "topic": r[4],
            "subtopic": r[5] or "",
            "difficulty": r[6],
            "tags": tags_list,
            "normalized_question": r[8],
            "time_complexity": r[9],
            "space_complexity": r[10],
            "code": r[11],
            "explanation": r[12] or ""
        })
    
    con.close()
    
    # 1. Save JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2)
    print(f"Exported {len(catalog)} entries to {output_json}")
    
    return catalog

if __name__ == '__main__':
    export_offline_catalog('data/solveai.db', 'data/catalog.json', 'src/services/catalogData.ts')
