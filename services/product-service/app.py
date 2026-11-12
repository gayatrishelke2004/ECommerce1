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


products = [
    {"id":1,"name":"iPhone 16"},
    {"id":2,"name":"Samsung S24"},
    {"id":3,"name":"Dell Inspiron"}
]

@app.get("/")
def home():
    return {"service":"Product Service"}

@app.get("/products")
def get_products():
    return products