import sqlite3


class Sqlite:
    def __init__(self, path:str) -> None:
        self.__con = sqlite3.connect(path)
        self.__cur = self.__con.cursor()
        self.__con.commit()


    def create_table(self, table:str , *args):
        self.__cur.execute(f"create table '{table}'{args}")
        self.__con.commit()


    def insert_one(self, table, *args):
        self.__cur.execute(f"insert into {table} values{args}")
        self.__con.commit()


    def insert_many(self, table, list):
        for i in list:
            self.__cur.execute(f"insert into {table} values{i}")
        self.__con.commit()


    def find_all(self, table):
        result = self.__cur.execute(f"select * from {table}")
        return result.fetchall()


    def find_one(self, table, pattern=False, **kargs):
        if pattern:
            r = tuple(*kargs.items())
            result = self.__cur.execute(f"select * from {table} where {r[0]} like '{r[1]}' ")
            return result.fetchall()
        else:
            r = tuple(*kargs.items())
            result = self.__cur.execute(f"select * from {table} where {r[0]} = '{r[1]}' ")
            return result.fetchall()




    
    def close(self):
        self.__con.close()    

    
        

db = Sqlite('sqlite_orm/sqlite.db')
# db.create_table('test', 'name', 'age')
# db.insert_many('test', [('hasan' , 15) , ('dwad',156)])
print(db.find_one('test', True, name = 'ha%'))
db.close()