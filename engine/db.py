import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null,'valorant','C:\\Riot Games\\Riot Client\\RiotClientServices.exe')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command (id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null,'linkedin','https://www.linkedin.com/in/pratyush-poddar-5b7aa6258/')"
# query = "INSERT INTO web_command VALUES(null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

# create a table with the desireed columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# SPECIFY THE COLUMNS
# desired_columns_indices =[0,18]

# # read data from csv and insert into SQLITE table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id,'name','mobile_no') VALUES (null, ?, ?); ''',tuple(selected_data))

# conn.commit()
# conn.close()


# DUMY NUMBER
# query = "INSERT INTO contacts VALUES (null,'pawan','1234567890','null')"
# cursor.execute(query)
# conn.commit()

## SEARCH 
query = 'Manas'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query +'%',query + '%'))
results = cursor.fetchall()
print(results[0][0])
