from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(id=1, name="John Doe")

@app.get("/users")
async def get_user():
    return user.dict()
