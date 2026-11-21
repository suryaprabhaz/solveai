import sqlite3
import json
import os
import glob
import re

def normalize_text(text):
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'[^\w\s,\.\-\+\#]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def import_batch(con, items):
    q_insert = """
    INSERT INTO questions (
        id, title, question, normalized_question, description, language,
        subject, topic, subtopic, difficulty, tags, input_format,
        output_format, constraints, sample_input, sample_output,
        explanation, time_complexity, space_complexity, source_type, verified
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        title=excluded.title,
        question=excluded.question,
        normalized_question=excluded.normalized_question,
        description=excluded.description,
        language=excluded.language,
        subject=excluded.subject,
        topic=excluded.topic,
        subtopic=excluded.subtopic,
        difficulty=excluded.difficulty,
        tags=excluded.tags,
        time_complexity=excluded.time_complexity,
        space_complexity=excluded.space_complexity,
        explanation=excluded.explanation,
        updated_at=CURRENT_TIMESTAMP
    """

    s_insert = """
    INSERT INTO solutions (
        id, question_id, language, code, explanation, algorithm,
        time_complexity, space_complexity, tested, test_cases
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        code=excluded.code,
        explanation=excluded.explanation,
        time_complexity=excluded.time_complexity,
        space_complexity=excluded.space_complexity
    """

    fts_delete = "DELETE FROM questions_fts WHERE id = ?"
    fts_insert = """
    INSERT INTO questions_fts (id, title, normalized_question, tags, language, subject, topic)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cur = con.cursor()
    inserted_q = 0
    inserted_s = 0

    for item in items:
        qid = item['id']
        title = item['title']
        q_text = item.get('question', title)
        norm_q = item.get('normalized_question') or normalize_text(f"{title} {q_text} {item.get('keywords', '')}")
        desc = item.get('description', '')
        lang = item['language'].lower().strip()
        subj = item.get('subject', 'Computer Science')
        topic = item.get('topic', 'General')
        subtopic = item.get('subtopic', '')
        diff = item.get('difficulty', 'Medium')
        tags_raw = item.get('tags', [])
        tags_str = ','.join(tags_raw) if isinstance(tags_raw, list) else str(tags_raw)
        inp_fmt = item.get('input_format', '')
        out_fmt = item.get('output_format', '')
        constraints = item.get('constraints', '')
        s_inp = item.get('sample_input', '')
        s_out = item.get('sample_output', '')
        expl = item.get('explanation', '')
        tc = item.get('time_complexity', 'O(1)')
        sc = item.get('space_complexity', 'O(1)')
        src = item.get('source_type', 'btech_curriculum')
        verified = item.get('verified', 1)

        cur.execute(q_insert, (
            qid, title, q_text, norm_q, desc, lang,
            subj, topic, subtopic, diff, tags_str, inp_fmt,
            out_fmt, constraints, s_inp, s_out,
            expl, tc, sc, src, verified
        ))
        inserted_q += 1

        # FTS Update
        cur.execute(fts_delete, (qid,))
        cur.execute(fts_insert, (qid, title, norm_q, tags_str, lang, subj, topic))

        # Solutions
        sol_id = f"sol-{qid}"
        code = item.get('code', '')
        algo = item.get('algorithm', '')
        test_cases = json.dumps(item.get('test_cases', []))

        cur.execute(s_insert, (
            sol_id, qid, lang, code, expl, algo,
            tc, sc, 1, test_cases
        ))
        inserted_s += 1

        # Tags table
        if isinstance(tags_raw, list):
            for t in tags_raw:
                t_clean = t.strip()
                if t_clean:
                    cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (t_clean,))
                    cur.execute("INSERT OR IGNORE INTO question_tags (question_id, tag_name) VALUES (?, ?)", (qid, t_clean))

    con.commit()
    return inserted_q, inserted_s

def import_all_batches(db_path, data_dir):
    from schema import init_db
    con = init_db(db_path)
    total_q = 0
    total_s = 0

    json_files = sorted(glob.glob(os.path.join(data_dir, '*.json')))
    print(f"Found {len(json_files)} batch JSON file(s) in {data_dir}")

    for jf in json_files:
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get('questions', [])
                q_cnt, s_cnt = import_batch(con, items)
                total_q += q_cnt
                total_s += s_cnt
                print(f"  -> Imported {len(items)} items from {os.path.basename(jf)}")
        except Exception as e:
            print(f"  [!] Failed to import {jf}: {e}")

    # Summary
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM questions")
    actual_q = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM solutions")
    actual_s = cur.fetchone()[0]
    cur.execute("SELECT language, COUNT(*) FROM questions GROUP BY language ORDER BY COUNT(*) DESC")
    by_lang = cur.fetchall()

    print("\n--- DATABASE IMPORT SUMMARY ---")
    print(f"Total Unique Questions: {actual_q}")
    print(f"Total Solutions:        {actual_s}")
    print("Breakdown by Language:")
    for l, cnt in by_lang:
        print(f"  - {l:15}: {cnt}")

    con.close()
    return actual_q

if __name__ == '__main__':
    db_file = os.path.join('data', 'solveai.db')
    data_folder = os.path.join('data', 'batches')
    import_all_batches(db_file, data_folder)
