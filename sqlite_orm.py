import sqlite3
from sqlite3 import OperationalError

class Sqlite:
    def __init__(self, path:str) -> None:
        self.__con = sqlite3.connect(path)
        self.__cur = self.__con.cursor()
        self.__con.commit()

    def create_table(self, name:str , *args):
        self.__cur.execute(f"create table '{name}'{args}")
        self.__con.commit()
            
        

    def insert_one(self, *args):
        self.__cur.execute(f"insert into test values{args}")
        self.__con.commit()
        






db = Sqlite('test/sqlite.db')
#db.create_table('test', 'name', 'age', 'job')
db.insert_one('ali', 20, 'doc' , 20)