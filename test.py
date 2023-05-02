import pymssql
import pandas as pd
from sqlalchemy import create_engine,text,engine

print('start')

server = '192.168.1.16\SQLEXPRESS'
database = 'test'
user_login = 'sa'
password = 'sa@admin'
query = 'select * from persons'

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+user_login+";PWD="+password+";"
connection_url = engine.URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine1 = create_engine(connection_url)

with engine1.begin() as conn:
    query_df = pd.read_sql_query(text(query), conn)
print(query_df)


print('start')
conn = pymssql.connect('192.168.100.11\SQLEXPRESS', 'sa', 'sa@admin', "test")

cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")

cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.'),
     (4, 'Mike T1.', 'Sarah H.')])

# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

#cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
cursor.execute('SELECT * FROM persons')
data=cursor.fetchall()
df=pd.DataFrame(data)

print(df)
conn.close()