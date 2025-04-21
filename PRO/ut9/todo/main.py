from __future__ import annotations
import sqlite3

def create_db(db_path:str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
    CREATE TABLE task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        done BOOLEAN
        )
    """
    cur.execute(sql)


class Task:
    con = sqlite3.connect('db_path')
    cur = con.cursor()
    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id
    
    def save(self) -> None:
        if self.id == -1:
            sql = "INSERT INTO task (name, done) VALUES (?, ?)"
            self.cur.execute(sql, (self.name, self.done))
            self.id = self.cur.lastrowid

    def update(self) -> None:
        sql = "UPDATE task SET name = ?, done = ? WHERE id = ?"
        self.cur.execute(sql, (self.name, self.done, self.id))

    def check(self) -> None:
        sql = "UPDATE task SET done = ? WHERE id = ?"
        self.cur.execute(sql, (True, self.id))
    
    def uncheck(self) -> None:
        sql = "UPDATE task SET done = ? WHERE id = ?"
        self.cur.execute(sql, (False, self.id))

    def __repr__(self):
        if self.done:
            return f"[x] {self.name} (id={self.id})"
        else:
            return f"[ ] {self.name} (id={self.id})"
    
    def from_db_row(cls, row: sqlite3.Row) -> 'Task':
        return cls(row['name'], row['done'], row['id'])
    
    def get(cls, task_id: int) -> Task:
        sql = "SELECT * FROM task WHERE id = ?"
        cls.cur.execute(sql, (task_id,))
        row = cls.cur.fetchone()
        if row:
            return cls.from_db_row(row)
        else:
            return None

class ToDo:
    con = sqlite3.connect('db_path')
    cur = con.cursor()
    
    def get_tasks(self, done: int = -1):
        if done == -1:
            sql = "SELECT * FROM task"
        elif done == 0:
            sql = "SELECT * FROM task WHERE done = 0"
        elif done == 1:
            sql = "SELECT * FROM task WHERE done = 1"
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
