import sqlite3

def get_connection(task_db = "task.db"):
    return sqlite3.connect(task_db)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            status INTEGER NOT NULL DEFAULT 0
        )
        """
    )    
    
    conn.commit()
    conn.close()
        
    
def add_task(description):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description, ))
    conn.commit()
    
    task_id = cursor.lastrowid
    conn.close()
    return task_id
    
def delete_task(id_task):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id_task,))
    
    success = cursor.rowcount > 0

    conn.commit()
    conn.close()
    
    return success
    
def show_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    
    conn.close()
    return result

def complete_task(id_task):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (1, id_task))
    
    success = cursor.rowcount > 0
        
    conn.commit()
    conn.close()
    
    return success


