from __future__ import annotations
import re
import sqlite3

DB_PATH = ':memory:'


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def create_db(self) -> None:
        sql ="""
            CREATE TABLE activity(
            id PRIMARY KEY,
            sender TEXT,
            recipient TEXT,
            message TEXT);

            CREATE TABLE access(
            phone_number PRIMARY KEY,
            pin TEXT,
            puk TEXT
            )
            ;
"""
        self.cur.executescript(sql)
        self.con.commit()
        
class SMS(DbHandler):
    
    def __init__(self, sender: str, recipient: str, message: str):
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.message = message
        

    def send(self) -> None:
        sql = 'INSERT INTO activity (sender, recipient, message) VALUES(?,?,?)'
        self.cur.execute(sql,(self.sender , self.recipient, self.message))
        self.con.commit()

    def __str__(self):
        return f'From: {self.sender}\nTo: {self.recipient}\n---\n{self.message}'

class SIM(DbHandler):

    def __init__(self, phone_number: str):
        super().__init__()
        self.phone_number = phone_number
        self.unlocked = False

    def unlock(self, pin: str, *, puk: str = '') -> None:
        sql = 'SELECT pin, puk FROM access WHERE phone_number=?'
        sim_data = self.cur.execute(sql,(self.phone_number,)).fetchone()
        correct_pin = sim_data['pin']
        correct_puk = sim_data['puk']
        if pin == correct_pin or puk == correct_puk:
            self.unlocked = True
        if not self.phone_number:
            self.unlocked = False
        
    @staticmethod
    def unlock_required(method):
        def wrapper(self,*args,**kwargs):
            if not self.unlocked:
                raise SMSError('SMS is locked', self)
            return method(self, *args, **kwargs)
        return wrapper        

    @unlock_required
    def send_sms(self, *, recipient: str, message: str) -> None:
        regxp = r'^\+?\d{2}?\s?[67]\d{8}$'
        if not re.match(regxp,recipient):
            raise SMSError('Recipient has invalid phone format', self)
        sms = SMS(self.phone_number,recipient,message)
        sms.send()

    @unlock_required
    def get_sms(self, sent: bool = True):
        sql_1 = 'SELECT * FROM activity WHERE sender =?'
        sql_2 = 'SELECT * FROM activity WHERE recipient =?'
        if sent:
            self.cur.execute(sql_1,(self.phone_number,))
        else:
            self.cur.execute(sql_2,(self.phone_number,))
        for row in self.cur.fetchall():
            yield (row['sender'],row['recipient'], row['message'])

class SMSError(Exception):
    def __init__(self, message: str, db_handler: DbHandler):
        super().__init__(message)
        db_handler.con.close()
