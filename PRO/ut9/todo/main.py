from __future__ import annotations
import sqlite3
DB_PATH = 'todo.db'

def create_db(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        done BOOLEAN
        )
    """
    cur.execute(sql)
    con.commit()
    con.close()


class Task:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id
    
    def save(self) -> None:
        sql = 'INSERT INTO tasks (name, done) VALUES (?, ?)'
        data = (self.name, self.done)
        Task.cur.execute(sql, data)
        self.id = Task.cur.lastrowid
        Task.con.commit()

    def update(self) -> None:
        sql = 'UPDATE tasks SET name = ?, done = ? WHERE id = ?'
        data = (self.name, self.done, self.id)
        Task.cur.execute(sql, data)
        Task.con.commit()

    def check(self) -> None:
        self.done = True
        self.update()

    def uncheck(self) -> None:
        self.done = False
        self.update()

    def __repr__(self):
        if self.done:
            return f"[X] {self.name} (id={self.id})"
        else:
            return f"[ ] {self.name} (id={self.id})"
    
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        return cls(row['name'], bool(row['done']), row['id'])
    
    @classmethod
    def get(cls, task_id: int) -> Task:
        sql = "SELECT * FROM tasks WHERE id = ?"
        cls.cur.execute(sql, (task_id,))
        row = cls.cur.fetchone()
        if row:
            return cls.from_db_row(row)
        else:
            return None


class ToDo:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    def get_tasks(self, done: int = -1):
        if done == -1:
            sql = "SELECT * FROM tasks"
        elif done == 0:
            sql = "SELECT * FROM tasks WHERE done = 0"
        elif done == 1:
            sql = "SELECT * FROM tasks WHERE done = 1"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            yield Task.from_db_row(row)
    
    def add_task(self, task: Task) -> None:
        task.save()
        self.con.commit()      

    def complete_task(self, task: Task) -> None:
        task.check()
        self.con.commit()

    def reopen_task(self, task: Task) -> None:
        task.uncheck()
        self.con.commit()
