from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "UP"}

@app.get("/api_two/cats")
async def root():
    return {"message": "Hello from CATS"}

@app.get("/api_two/dogs")
async def root():
    return {"message": "Hello from DOGS"}