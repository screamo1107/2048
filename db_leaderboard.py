import sqlite3


bd = sqlite3.connect("2048.sqlite")
crsr = bd.cursor()
crsr.execute("""
    CREATE TABLE IF NOT EXISTS records (
        name text,
        score integer
    )
""")


def get_best_results():
    crsr.execute("""
        SELECT name, max(score) score
        FROM records
        GROUP BY name
        ORDER BY score DESC
        LIMIT 3
    """)
    return crsr.fetchall()


def insert_result(name: str, score: int):
    crsr.execute("""
        INSERT INTO records
        VALUES (?, ?)
    """, (name, score))
    bd.commit()
