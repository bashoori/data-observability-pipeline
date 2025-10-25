import sqlite3, json, os

DB_PATH = os.path.join(os.getcwd(), "data", "analytics.db")

def load_to_sqlite():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        price REAL,
        rating REAL
    )
    """)

    with open("/tmp/clean_data.json") as f:
        records = json.load(f)

    cur.executemany("""
        INSERT OR REPLACE INTO products (id, title, category, price, rating)
        VALUES (:id, :title, :category, :price, :rating)
    """, records)

    conn.commit()
    conn.close()
    print("✅ Data loaded into SQLite successfully")
