from dotenv import load_dotenv
import os
import psycopg


def get_connection():
    load_dotenv()

    connection=psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return connection

if __name__ == "__main__":

    with get_connection() as conn:
    
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            products=cur.fetchall()

            for product in products:
                print(product[0], product[1])

