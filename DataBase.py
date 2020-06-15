import sqlite3

dbase = sqlite3.connect('data base.db')
dbase.execute(''' CREATE TABLE IF NOT EXISTS daataa(
            ID INT PRIMARY KEY NOT NULL,
            FOOTBALL TEXT NOT NULL,
            FOOTBALL1 TEXT NOT NULL,
            FOOTBALL2 TEXT NOT NULL) ''')
dbase.execute(''' INSERT INTO daataa(ID,FOOTBALL,FOOTBALL1,FOOTBALL2)
        VALUES (1,'ZAMALEK','WHITE','MOHAMED')''')
dbase.commit()
dbase.close()