import re
import sqlite3

DB_PATH = ':memory:'


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def create_db(self) -> None:
        sql = """
            CREATE TABLE login(
            username TEXT PRIMARY KEY,
            password TEXT,
            domain TEXT
            );

            CREATE TABLE activity(
            id INTEGER PRIMARY KEY,
            sender TEXT,
            recipient TEXT,
            subject TEXT,
            body TEXT
            );
        """
        self.cur.executescript(sql)
        self.con.commit()
        
class Mail(DbHandler):
    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self) -> None:
        sql = 'INSERT INTO activity (sender, recipient, subject, body) VALUES (?,?,?,?)'
        self.cur.execute(sql, (self.sender, self.recipient, self.subject, self.body))
        self.con.commit()

    def __str__(self):
        return f'From: {self.sender}\nTo: {self.recipient}\n---\n{self.subject.upper()}\n{self.body}'


class MailServer(DbHandler):
    def __init__(self, username: str):
        super().__init__()
        self.username = username
        self.logged = False

    def login(self, password: str) -> None:
        sql = 'SELECT * FROM login WHERE username=?'
        self.cur.execute(sql, (self.username,))
        data = self.cur.fetchone()
        if data and data['password'] == password:
            self.domain = data['domain']
            self.logged = True
        else:
            self.logged = False
            self.domain = ''
            
    @staticmethod
    def login_required(method):
        def wrapper(self, *args, **kwargs):
            if not self.logged:
                raise MailError('User is not logged in', self)
            return method(self, *args, **kwargs)
        return wrapper

    @property
    def sender(self) -> str:
        return f'{self.username}@{self.domain}'

    @login_required
    def send_mail(self, *, recipient: str, subject: str, body: str) -> None:
        regexp = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        if re.fullmatch(regexp, recipient, re.I):
            mail = Mail(self.sender, recipient, subject, body)
            mail.send()
        else:
            raise MailError('Recipient has invalid mail format', self)

    @login_required
    def get_emails(self, sent: bool = True):
        if sent:
            sql = 'SELECT * FROM activity WHERE sender=?'
        else:
            sql = 'SELECT * FROM activity WHERE recipient=?'
        self.cur.execute(sql, (self.sender,))
        emails = self.cur.fetchall()
        for email in emails:
            yield Mail(email['sender'], email['recipient'], email['subject'], email['body'])

class MailError(Exception):
    def __init__(self, message: str, db_handler: DbHandler):
        super().__init__(message)
        db_handler.con.close()
        
##c