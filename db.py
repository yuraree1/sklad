from dotenv import load_dotenv
import os
import psycopg


load_dotenv()

with psycopg.connect(
dbname=os.getenv("DB_NAME"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWORD"),
host=os.getenv("DB_HOST"),
port=os.getenv("DB_PORT")
) as conn:
    
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM products")
        products=cur.fetchall()
        
        for product in products:
            print(product[0], product[1])

