from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    host="postgres-service",
    database="retaildb",
    user="postgres",
    password="postgres"
)

@app.get("/")
def home():
    return {
        "service": "Search Service"
    }


@app.get("/search")
def search_product(q: str):

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id,name,price
        FROM products
        WHERE LOWER(name) LIKE LOWER(%s)
        """,
        (f"%{q}%",)
    )

    products = cursor.fetchall()

    result = []

    for product in products:
        result.append({
            "id": product[0],
            "name": product[1],
            "price": product[2]
        })

    return result