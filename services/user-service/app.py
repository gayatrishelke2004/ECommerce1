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

    conn = psycopg2.connect(
        host="postgres",
        database="retaildb",
        user="postgres",
        password="postgres"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,name,email FROM users"
    )

    users = cursor.fetchall()

    return users