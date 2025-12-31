from fastapi import FastAPI

app = FastAPI()

@app.get("/health")

def health():

    return {"status": "ok"}

@app.get("/")

def root():

    return {"message": "DevOps Local Project Running"}
