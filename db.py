import mysql.connector as sqc

db = sqc.connect(host="localhost",user="blunt",password="Zomboy8897")

cursor = db.cursor()
cursor.execute("CREATE DATABASE testdatabase") 