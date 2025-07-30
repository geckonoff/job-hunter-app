from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Job Hunter API Gateway")

@app.get("/")
def read_root():
    return {"message": "Job Hunter API Gateway is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
