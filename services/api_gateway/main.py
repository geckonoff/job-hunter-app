from fastapi import FastAPI

app = FastAPI(title="Job Hunter API Gateway")

@app.get("/")
def read_root():
    return {"message": "Welcome to Job Hunter API Gateway"}
