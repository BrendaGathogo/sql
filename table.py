import sqlite3
conn=sqlite3.connect('backupdb')
print("Successfully opened")
conn.execute("CREATE TABLE Clothes"
             "(ID INT PRIMARY KEY NOT NULL,"
             "TYPE TEXT NOT NULL,"
             "BRAND TEXT NOT NULL,"
             "PRICE INT NOT NULL) ")
print("Table created")
conn.close()