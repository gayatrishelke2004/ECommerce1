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