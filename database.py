import sqlite3

def init_db():
    conn = sqlite3.connect("juegos.db")
    cursor = conn.cursor()

    # Crear tabla
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS juegos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        imagen TEXT NOT NULL,
        precio REAL NOT NULL
    )
    ''')

    # Insertar juegos de ejemplo
    cursor.execute("INSERT OR IGNORE INTO juegos (id, nombre, imagen, precio) VALUES (1, 'Elden Ring', 'elden.jpg', 30000)")
    cursor.execute("INSERT OR IGNORE INTO juegos (id, nombre, imagen, precio) VALUES (2, 'Mortal Kombat 1', 'mortal.jpg', 25000)")
    cursor.execute("INSERT OR IGNORE INTO juegos (id, nombre, imagen, precio) VALUES (3, 'Total War: Warhammer 3', 'total.jpg', 20000)")

    conn.commit()
    conn.close()
    print(" Base de datos creada y lista.")

if __name__ == "__main__":
    init_db()
