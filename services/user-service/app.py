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
        "service": "User Service"
    }


@app.get("/users")
def get_users():

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,name,email FROM users"
    )

    users = cursor.fetchall()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })

    return result