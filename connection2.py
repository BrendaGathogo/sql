import sqlite3
conn=sqlite3.connect('backupdb')
print("Successfully opened")

conn.execute("INSERT INTO Clothes(ID,TYPE,BRAND,PRICE) VALUES (1,'Shoes','addidas',4000)")
conn.execute("INSERT INTO Clothes(ID,TYPE,BRAND,PRICE) VALUES (2,'Shirt','LCWaikiki',2000)")
conn.execute("INSERT INTO Clothes(ID,TYPE,BRAND,PRICE) VALUES (3,'Trouser','City',6000)")

conn.commit()
print("records added")
conn.close()