import pymssql
import pandas as pd
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