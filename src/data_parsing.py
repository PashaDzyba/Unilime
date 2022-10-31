import psycopg2
import psycopg2.extras as extras
import pandas as pd


def execute_values(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("The CSVData is inserted")
    cursor.close()


conn = psycopg2.connect(
    database="devdb", user='postgres', password='password', host='127.0.0.1', port='5432'
)

df = pd.read_csv('products.csv')
df2 = pd.read_csv('reviews.csv')
execute_values(conn, df, 'products')
execute_values(conn, df2, 'reviews')



