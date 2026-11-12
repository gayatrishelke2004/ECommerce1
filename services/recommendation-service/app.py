from fastapi import FastAPI

app = FastAPI()

recommendations = {
    "iphone":["AirPods","Apple Watch"],
    "samsung":["Galaxy Watch","Galaxy Buds"],
    "dell":["Wireless Mouse","Keyboard"]
}

@app.get("/")
def home():
    return {"service":"Recommendation Service"}

@app.get("/recommend/{product}")
def recommend(product:str):

    return {
        "recommendations":
        recommendations.get(product.lower(),[])
    }