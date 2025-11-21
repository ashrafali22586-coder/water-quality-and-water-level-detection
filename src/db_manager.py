import sqlite3

def get_all_results(db="water_quality.db"):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM results")
    rows = cur.fetchall()
    conn.close()
    return rows
