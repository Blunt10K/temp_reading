import mysql.connector as sqc

def create_database(cursor, name):
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        if(x[0]==name):
            print("Database already exists.")
            return
    print("Creating new database: " + name)
    cmnd = "CREATE DATABASE " + name
    cursor.execute(cmnd)

    return

class Database:
    
    # @staticmethod


    def __init__(self,user,password,name):
        self.db = sqc.connect(host="localhost",user=user,password=password)
        self.cursor = self.db.cursor()
        self.name = name
        create_database(self.cursor,name)


