import pymssql
import pandas as pd
from sqlalchemy import create_engine,text,engine

print('start')

server = '192.168.100.11\SQLEXPRESS'
database = 'test'
user_login = 'sa'
password = 'sa@admin'
query = 'select * from persons'

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+user_login+";PWD="+password+""
connection_url = engine.URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine1 = create_engine(connection_url)

with engine1.begin() as conn:
    query_df = pd.read_sql_query(text(query), conn)
print(query_df)