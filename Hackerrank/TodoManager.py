import sqlite3
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TodoItem:
    id: Optional[int]
    title: str
    description: str
    completed: bool
    created_at: str
    due_date: Optional[str]

class TodoManager:
    def __init__(self, db_name='todo.db'):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Initialize database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                created_at TEXT NOT NULL,
                due_date TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def add_todo(self, title, description="", due_date=None):
        """Add new todo item"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        created_at = datetime.now().isoformat()
        cursor.execute('''
            INSERT INTO todos (title, description, completed, created_at, due_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, False, created_at, due_date))
        
        conn.commit()
        todo_id = cursor.lastrowid
        conn.close()
        
        return self.get_todo(todo_id)
    
    def get_todo(self, todo_id):
        """Get single todo item"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return TodoItem(*row)
        return None
    
    def get_all_todos(self, completed=None):
        """Get all todo items, optionally filtered by completion"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        if completed is None:
            cursor.execute('SELECT * FROM todos ORDER BY created_at DESC')
        else:
            cursor.execute('SELECT * FROM todos WHERE completed = ? ORDER BY created_at DESC', 
                         (completed,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [TodoItem(*row) for row in rows]
    
    def update_todo(self, todo_id, **kwargs):
        """Update todo item"""
        allowed_fields = ['title', 'description', 'completed', 'due_date']
        updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not updates:
            return False
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        set_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
        values = list(updates.values()) + [todo_id]
        
        cursor.execute(f'UPDATE todos SET {set_clause} WHERE id = ?', values)
        conn.commit()
        conn.close()
        
        return cursor.rowcount > 0
    
    def delete_todo(self, todo_id):
        """Delete todo item"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        
        return deleted

# Usage
todo_manager = TodoManager()

# Add todo
todo = todo_manager.add_todo("Learn Python", "Complete advanced Python course", "2024-12-31")
print(f"Added todo: {todo.title}")

# Get all pending todos
pending = todo_manager.get_all_todos(completed=False)
print(f"You have {len(pending)} pending todos")

# Mark as complete
todo_manager.update_todo(todo.id, completed=True)