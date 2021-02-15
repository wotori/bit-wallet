from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/async")
async def async_test():
    return ["Hello", "World"]