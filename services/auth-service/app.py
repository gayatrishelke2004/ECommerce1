from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/")
def home():
    return {"service": "Auth Service"}

@app.post("/register")
def register(user: dict):
    users.append(user)
    return {"message": "User Registered"}

@app.post("/login")
def login():
    return {"token":"sample-jwt-token"}