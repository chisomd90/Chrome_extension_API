import sqlite3

def create_database():
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()
    
    # Create a table to store video metadata
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id TEXT PRIMARY KEY,
            filename TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()