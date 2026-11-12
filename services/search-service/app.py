from fastapi import FastAPI
import psycopg2

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"service": "Search Service"}

@app.get("/search")
def search_product(q: str):

    conn = psycopg2.connect(
        host="postgres",
        database="retaildb",
        user="postgres",
        password="postgres"
    )

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
            "price": float(product[2])
        })

    cursor.close()
    conn.close()

    return result