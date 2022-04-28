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


    def update(self, table, set:dict, where:dict, pattern=False):
        
        if pattern:
            s = tuple(set.items())[0]
            w = tuple(where.items())[0]
            self.__cur.execute(f" update {table} set {s[0]} = '{s[1]}' where {w[0]} like '{w[1]}' ")
            self.__con.commit()
        else:
            s = tuple(set.items())[0]
            w = tuple(where.items())[0]
            self.__cur.execute(f" update {table} set {s[0]} = '{s[1]}' where {w[0]} = '{w[1]}' ")
            self.__con.commit()


    def delete_item(self, table, pattern=False, **kargs):
        if pattern:
            r = tuple(*kargs.items()) 
            self.__cur.execute(f"delete from {table} where {r[0]} like '{r[1]}' ")
            self.__con.commit()
        else:
            r = tuple(*kargs.items())
            self.__cur.execute(f"delete from {table} where {r[0]} = '{r[1]}' ")
            self.__con.commit()


    def delete_table(self, table):
        self.__cur.execute(f"drop table {table}")



    def close(self):
        self.__con.close()    

    
        

