import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']


def inseredg(data):
    # data = [(5, 'One Plus 6', 950),(5, 'One Plus 6', 950)]
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        # create table one by one
        insert_query = """ INSERT INTO dadosgerais (data,acoes,fii,reits,rfixa,rvalor,stocks) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        for registro in data:
            cur.execute(insert_query, registro)        
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def apagatb(table_name):
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        # create table one by one
        qrapaga = "DROP TABLE %s;" % (table_name,)
        cur.execute(qrapaga)        
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insereaportes(data):
    # data = [(5, 'One Plus 6', 950),(5, 'One Plus 6', 950)]
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        # create table one by one
        insert_query = """ INSERT INTO tbaportes (data,acoes,fii,reits,rfixa,rvalor,stocks) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        for registro in data:
            cur.execute(insert_query, registro)        
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()