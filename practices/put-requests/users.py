from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str


USERS = [
    {"id": 1, "name": "User One", "email": "user1@example.com"},
    {"id": 2, "name": "User Two", "email": "user2@example.com"},
    {"id": 3, "name": "User Three", "email": "user3@example.com"},
    {"id": 4, "name": "User Four", "email": "user4@example.com"},
    {"id": 5, "name": "User Five", "email": "user5@example.com"},
]


@app.get("/users")
async def get_all_user():
    return USERS


@app.put("/users/{user_id}")
async def update_user(user_id : int, updated_user: User):
    for user in USERS:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email
            return user
    return {"error" : "User is not Found!"}

        