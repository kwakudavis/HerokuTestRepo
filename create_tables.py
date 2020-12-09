import sqlite3

connection  = sqlite3.connect('data.db') #Sqlite connects to a singulare file, but mind you its slower 

cursor = connection.cursor() #The cursor is used to select things and start things 


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username  text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY , name  text, price real)" #real is a float
cursor.execute(create_table)


connection.commit()

connection.close()