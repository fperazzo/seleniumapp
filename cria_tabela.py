import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = ("""CREATE TABLE geral (
            geral_id SERIAL PRIMARY KEY,
            geral_data datetime NOT NULL,
            geral_acoes real NOT NULL)
            """,
            """ CREATE TABLE aportes (
            aportes_id SERIAL PRIMARY KEY,
            aportes_name VARCHAR(255) NOT NULL)
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



create_tables()
