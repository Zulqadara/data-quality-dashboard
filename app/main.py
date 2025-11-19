import fastapi

app = fastapi.FastAPI()

@app.get("/")
def test():
    return {"Hello": "World"}