import mysql.connector as sqc

db = sqc.connect(host="localhost",user="blunt",password="password")

cursor = db
cursor.execute("CREAT DATABASE tempdatabase")