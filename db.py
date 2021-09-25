import mysql.connector as sqc

class Database:
    def __init__(self,user,password,name):
        self.db = sqc.connect(host="localhost",user=user,password=password)
        self.cursor = self.db.cursor()
        self.cursor.execute("")

    @staticmethod
    def create_database(cursor, name):
        cursor.execute("SHOW DATABASES")
        return
        i = 0
        for x in cursor:
            if(x[i]==name):
                print("Database already exists.")
                return
            i+=1
        print("Creating new database: " + name)
        cmnd = "CREATE DATABASE " + name
        cursor.execute(cmnd)

        return
