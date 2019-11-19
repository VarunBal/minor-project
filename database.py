import psycopg2 as pg
import numpy as np

conn = pg.connect(database="project", user="postgres", password="root", host="localhost", port="5432")

db_cur = conn.cursor()

def food_data(name):
    try:
        db_cur.execute("SELECT * FROM FOOD WHERE NAME = '%s';"%name)
        data = db_cur.fetchall()
        return data
    except Exception as e:
        print(e)

def close_conn():
    conn.close()

def main():
    db_cur.execute("SELECT * FROM FOOD;")
    data = db_cur.fetchall()
    print('data length:',len(data))
    conn.close()

if __name__ == '__main__':
    main()
