from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Churn Prediction API", description="API for predicting customer churn", version="1.0")

@app.get("/ping")
def ping():
    return "PONG"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)