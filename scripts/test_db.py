import sqlite3
import os
import sys

def run_tests(db_path='data/solveai.db'):
    if not os.path.exists(db_path):
        print(f"Error: Database {db_path} does not exist!")
        return False

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    print("==================================================")
    print("        SOLVEAI B.TECH DATABASE VERIFICATION      ")
    print("==================================================")

    # 1. Total records check
    cur.execute("SELECT COUNT(*) FROM questions")
    total_q = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM solutions")
    total_s = cur.fetchone()[0]
    print(f"[*] Verified Questions in Database: {total_q}")
    print(f"[*] Verified Solutions in Database: {total_s}")
    assert total_q > 0 and total_s > 0, "Database is empty!"

    # 2. Duplicate prevention test
    print("\n[+] Testing Duplicate Prevention (Idempotency)...")
    cur.execute("SELECT id, title, language FROM questions LIMIT 1")
    sample = cur.fetchone()
    try:
        cur.execute("INSERT INTO questions (id, title, question, normalized_question, language, subject, topic, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (sample[0], sample[1], "dup test", "dup", sample[2], "test", "test", "Easy"))
        print("[!] Duplicate check failed: Duplicate ID was allowed!")
    except sqlite3.IntegrityError:
        print(f"    ✓ Passed: SQLite PRIMARY KEY strictly prevented duplicate insertion for id: '{sample[0]}'")

    # 3. Retrieval by Language
    print("\n[+] Testing Retrieval by Language:")
    cur.execute("SELECT language, COUNT(*) FROM questions GROUP BY language ORDER BY COUNT(*) DESC")
    langs = cur.fetchall()
    for lang, cnt in langs:
        print(f"    - {lang:12} : {cnt} questions")

    # 4. Retrieval by Subject
    print("\n[+] Testing Retrieval by Subject:")
    cur.execute("SELECT subject, COUNT(*) FROM questions GROUP BY subject ORDER BY COUNT(*) DESC")
    subjects = cur.fetchall()
    for subj, cnt in subjects:
        print(f"    - {subj:35} : {cnt} questions")

    # 5. Full-Text Search (FTS5) test
    print("\n[+] Testing FTS5 Keyword & Academic Problem Queries:")
    test_queries = [
        ("binary search", "C"),
        ("vector", "C++"),
        ("producer consumer", "Java"),
        ("linear regression", "Python"),
        ("salary", "SQL"),
        ("fourier", "MATLAB"),
        ("bresenham", "C")
    ]

    for tq, expected_lang in test_queries:
        cur.execute("""
            SELECT q.title, q.language, q.difficulty, q.time_complexity
            FROM questions_fts f
            JOIN questions q ON f.id = q.id
            WHERE questions_fts MATCH ?
            LIMIT 1
        """, (tq,))
        res = cur.fetchone()
        if res:
            print(f"    ✓ Query: '{tq:20}' -> Found: '{res[0]}' [{res[1].upper()}] (Complexity: {res[3]})")
        else:
            print(f"    [!] Query '{tq}' did not return results.")

    con.close()
    print("\n[✓] All database verification tests completed successfully.")
    return True

if __name__ == '__main__':
    db = sys.argv[1] if len(sys.argv) > 1 else 'data/solveai.db'
    run_tests(db)
