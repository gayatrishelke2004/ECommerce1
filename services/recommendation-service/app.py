from fastapi import FastAPI
from database import recommendation_collection

app = FastAPI()

@app.get("/")
def home():
    return {"service": "Recommendation Service"}

@app.post("/recommend")
def save_recommendation():

    data = {
        "user_id": 1,
        "recommended_products": [
            "Laptop",
            "Mobile"
        ]
    }

    recommendation_collection.insert_one(data)

    return {"message": "Recommendation saved"}

@app.get("/recommend/{user_id}")
def get_recommendation(user_id: int):

    recommendation = recommendation_collection.find_one(
        {"user_id": user_id},
        {"_id": 0}
    )

    if recommendation:
        return recommendation

    return {"message": "No recommendation found"}