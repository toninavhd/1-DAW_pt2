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
        username TEXT UNIQUE,
        password TEXT,
        bio TEXT
        );
    CREATE TABLE tweet (
        id INTEGER PRIMARY KEY,
        content TEXT,
        user_id INTEGER REFERENCES user(id),
        retweet_from INTEGER REFERENCES tweet(id)
        );
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
        self.id = user_id
        self.logged = False
    
    def __repr__(self):
        return f'{self.username}: {self.bio}'
    
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> User:
        return cls(row['username'], row['password'], row['bio'], row['id'])

    @property
    def tweets(self):
        sql = 'SELECT * FROM tweet WHERE user_id = ?'
        for row in User.cur.execute(sql, (self.id,)):
            yield Tweet.from_db_row(row)

    def save(self) -> None:
        sql = 'INSERT INTO user (username, password, bio) VALUES (?, ?, ?)'
        data = (self.username, self.password, self.bio)
        User.cur.execute(sql, data)
        User.con.commit()
        self.id = User.cur.lastrowid
        
    def login(self, password: str) -> bool:
        sql = 'SELECT * FROM user WHERE username = ? AND password = ?'
        User.cur.execute(sql, (self.username, password))
        if User.cur.fetchone() is not None:
            self.logged = True
            return True
        self.logged = False
        return False

    def tweet(self, content: str) -> Tweet:
        MAX_TW_LEN = 280

        if not self.logged:
            raise TwitterError(f'User {self.username} is not logged in!')
        if len(content) > MAX_TW_LEN:
            raise TwitterError(f'Tweet has more than {MAX_TW_LEN} chars!')
        new_tweet = Tweet(content, self.id)
        new_tweet.save()
        return new_tweet
    
    def retweet(self, tweet_id: int) -> Tweet:
        if not self.logged:
            raise TwitterError(f'User {self.username} is not logged in!')
        if tweet_id not in [Tweet.id for Tweet in self.tweets]:
            raise TwitterError(f'Tweet with id {tweet_id} does not exist!')
        new_retweet = Tweet(retweet_from=tweet_id, user_id=self.id)
        new_retweet.save()
        return new_retweet
    
class Tweet:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, content: str = '', user_id: int = 0, retweet_from: int = 0, tweet_id: int = 0):
        self._content = content
        self.user_id = user_id
        self.retweet_from = retweet_from
        self.id = tweet_id
    
    def __repr__(self):
        if self.retweet_from != 0:
            return f'[RT] {self.content} (id={self.id})'
        return f'{self.content} (id={self.id})'
    
    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        return cls(row['content'], row['user_id'], row['retweet_from'], row['id'])
    
    @property
    def content(self) -> str:
        if self.retweet_from != 0:
            sql = 'SELECT content FROM tweet WHERE id = ?'
            result = Tweet.cur.execute(sql, (self.retweet_from,)).fetchone()
            return result['content'] if result else ''
        return self._content
    
    @property
    def is_retweet(self) -> bool:
        return self.retweet_from != 0

    def save(self, user: User = None) -> None:
        if user:
            self.user_id = user.id

        sql = 'INSERT INTO tweet (content, user_id, retweet_from) VALUES (?, ?, ?)'
        data = (self._content, self.user_id, self.retweet_from)
        Tweet.cur.execute(sql, data)
        Tweet.con.commit()
        self.id = Tweet.cur.lastrowid
    
class Twitter:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def add_user(self, username: str, password: str, bio: str = '') -> User:
        password_regxp = r'[@=]\d{2,4}[a-z]{2,4}[!*]'
        if not re.match(password_regxp, password, re.I):
            raise TwitterError('Password does not follow security rules!')
        new_user = User(username, password, bio)
        new_user.save()
        return new_user

    def get_user(self, user_id: int) -> User:
        sql = 'SELECT * FROM user WHERE id = ?'
        if match := self.cur.execute(sql, (user_id,)).fetchone():
            return User.from_db_row(match)
        raise TwitterError(f'User with id {user_id} does not exist!')

class TwitterError(Exception):
    pass