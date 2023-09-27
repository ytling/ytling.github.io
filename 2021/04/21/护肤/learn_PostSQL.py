import psycopg2
from config import config


# read connection parameters
params = config()

# connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(
    database="myDB",
    user="postgres",
    password="008820@Sql")
		
# create a cursor
cur = conn.cursor()
        
# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

 # display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
