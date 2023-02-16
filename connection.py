import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened bd successfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (1,'Erick',30,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (2,'Brenda',18,'Modcom')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (3,'Samantha',34,'UON')")

conn.commit()
print("records added successfully")
conn.close()