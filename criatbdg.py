import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

""" create tables in the PostgreSQL database"""
command = ("""CREATE TABLE dadosgerais (
        id SERIAL PRIMARY KEY,
        data timestamp NOT NULL,
        acoes real NOT NULL,
        fii real NOT NULL,
        reits real NOT NULL,
        rfixa real NOT NULL,
        rvalor real NOT NULL,
        stocks real NOT NULL,)
        """)
conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()