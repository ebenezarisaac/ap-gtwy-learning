from fastapi import FastAPI

app = FastAPI()


@app.get("/cats")
async def root():
    return {"message": "Hello from CATS"}

@app.get("/dogs")
async def root():
    return {"message": "Hello from DOGS"}