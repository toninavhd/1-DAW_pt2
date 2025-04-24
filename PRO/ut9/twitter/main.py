from __future__ import annotations

import re
import sqlite3

DB_PATH = 'twitter.db'

def create_db(db_path: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """
    CREATE TABLE user (
        id INTEGER PRIMARY KEY,
        username UNIQUE TEXT,
        password TEXT,
        bio TEXT
        )
    CREATE TABLE tweet (
        id INTEGER PRIMARY KEY,
        content TEXT,
        user_id INTEGER REFERENCES user(id),
        retweet_from INTEGER REFERENCES tweet(id)
        )
    """
    cur.executescript(sql)
    con.commit()
    con.close()
    

class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, password: str, bio: str = '', user_id: int = 0):
        self.username = username
        self.password = password
        self.bio = bio
        self.user_id = user_id
        self.logged = False
    
    def save(self) -> None:
        sql = 'INSERT INTO user (username, password, bio) VALUES (?, ?, ?)'
        data = (self.username, self.password, self.bio)
        User.cur.execute(sql, data)
        User.con.commit()
        self.user_id = self.cur.lastrowid 
        
    
    def login(self, password: str) -> None:
        if self.password == password:
            self.logged = True
    
    def tweet(self, content: str) -> Tweet:
        if not self.logged:
            raise TwitterError("User not logged in")
        if len(content) > 280:
            raise TwitterError("Tweet has more than 280 chars")
        new_tweet = Tweet(content, self.user_id)
        new_tweet.save()
        return new_tweet
    
    def __repr__(self):
        return f'{self.username}: {self.bio})'
    
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> User:
        return cls(row['username'], row['password'], row['bio'], row['id'])

    @property
    def tweets(self):
        sql = 'SELECT * FROM tweet WHERE user_id = ?'
        for row in User.cur.execute(sql, (self.user_id,)):
            yield Tweet.from_db_row(row)

class Tweet:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, content: str = '', retweet_from: int = 0, tweet_id: int = 0):
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.content = content
        self.retweet_from = retweet_from
        self.tweet_id = tweet_id

    def save(self) -> None:
        sql = 'INSERT INTO tweet (contetnt, user_id, retweet_from) VALUES (?, ?, ?)'
        data = (self.content, self.user_id, self.retweet_from)
        self.cur.execute(sql, data)
        self.tweet_id = self.cur.lastrowid
        self.con.commit()

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        return cls(row['content'], row['retweet_from'], row['id'])
    
    @property
    def content(self) -> str:
        if self.retweet_from != 0:
            sql = 'SELECT content FROM tweet WHERE id = ?'
            self.content = Tweet.cur.execute(sql, (self.retweet_from,)).fetchone()['content']
        return self.content
    
    @property
    def is_retweet(self) -> bool:
        return self.retweet_from != 0
    
    def __repr__(self):
        if self.retweet_from != 0:
            return f'[RT] {self.content} (id={self.tweet_id})'
        else:
            return f'{self.content} (id={self.tweet_id})'
        
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        return cls(row['content'], row['retweet_from'], row['id'])
    
class Twitter:
    con = sqlite3.connect('twitter.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    def add_user(self, username: str, password: str, bio: str = '') -> User:
        password_regxp = r'[@=]\d{2,4}[a-z]{2,4}[!*]$'
        if not re.match(password_regxp, password):
            raise TwitterError('Password does not follow security rules!')
        new_user = User(username, password, bio)
        new_user.save()
        return new_user

    def get_user(self, user_id: int) -> User:
        sql = 'SELECT * FROM user WHERE id = ?'
        if match := self.cur.execute(sql, (user_id,)).fetchone():
            return User.from_db_row(match)
        raise TwitterError('User with id {user_id} does not exist')

class TwitterError(Exception):
    def __init__(self, message=''):
        value = message
        super().__init__(value)


