# PUT Request

## Introduction
A PUT request is an HTTP method used to **update/replace an existing resource** at a known URL. Unlike POST, it targets a specific resource by ID and is idempotent — calling it multiple times with the same data produces the same result.

## Syntax
```python
@app.put("/path/{id}")
async def function_name(id: int, payload: SomeModel):
    return payload
```

## Why
- Updates an existing resource instead of creating a new one
- Idempotent — repeating the same request doesn't create duplicates or change the outcome
- URL identifies exactly which resource is being updated (`/users/{id}`)

## How
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for user in USERS:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email
            return user
    return {"error": "User is not Found!"}
```
- `user_id` (path param) → identifies **which** resource to update
- `updated_user: User` (body) → the new data to apply
- Loop through the in-memory list to find the matching record (no DB here, so manual lookup is needed)
- Only fields declared in the model (here: `name`, `email`) are required in the body

## When
Use PUT when the client is **updating/replacing** an existing resource:
- `/users/{id}`
- `/books/{id}`
- `/orders/{id}`

Not for creating new resources (`POST`), not for just reading (`GET`).

## Analogy
Like replacing the contents of an existing file folder with a new one, using the folder's label (ID) to find it. You're not creating a new folder — you're swapping what's inside the one that's already there.