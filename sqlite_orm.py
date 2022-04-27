import sqlite3


class Sqlite:
    def __init__(self, path:str) -> None:
        self.__con = sqlite3.connect(path)
        self.__cur = self.__con.cursor()
        self.__con.commit()


    def create_table(self, name:str , *args):
        self.__cur.execute(f"create table '{name}'{args}")
        self.__con.commit()


    def insert_one(self, name,*args):
        self.__cur.execute(f"insert into {name} values{args}")
        self.__con.commit()


    def insert_many(self, name, list):
        for i in list:
            self.__cur.execute(f"insert into {name} values{i}")
        self.__con.commit()









    
    def close(self):
        self.__con.close()    

    
        

db = Sqlite('sqlite_orm/sqlite.db')
#db.create_table('test', 'name', 'age')
db.insert_many('test', [('hasan' , 15) , ('dwad',156)])
db.close()