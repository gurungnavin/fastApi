# Path Parameters

## Introduction
A path parameter is a variable part of a URL used to identify a specific resource, defined with curly braces in the route (e.g. `/users/{user_id}`).

## Syntax
```python
@app.get("/path/{parameter_name}")
async def function_name(parameter_name: type):
    return {"parameter_name": parameter_name}
```    

## Why
- Avoids writing one route per resource
- Lets the server fetch only the exact resource needed, instead of fetching everything and filtering after
- Makes URLs read naturally: `/users/123` = "the user with ID 123"
- Required by definition — the route won't match without it

## How
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```
- `{user_id}` → placeholder in the route
- `user_id: int` → FastAPI validates/converts the value automatically
- `/users/123` → `user_id = 123`
- `/users/abc` → 422 validation error

## When
Use it when the value identifies **which** specific resource you're acting on:
- `/users/{id}`
- `/products/{id}`
- `/orders/{id}`

Not for optional filtering/searching — that's what query parameters are for (`/users?active=true`).

## Server-start command

**Option 1: cd into the folder**
cd practices/path-parameters
uvicorn books:app --reload

**Option 2: run from repo root (fastApi/)**
uvicorn practices.path-parameters.books:app --reload

- Works even though `path-parameters` has a hyphen — uvicorn resolves the
  module path via `importlib.import_module()`, which looks up folders by
  name on disk (hyphens allowed there). The hyphen only breaks a literal
  `import practices.path-parameters.books` statement in Python source code.

- No `__init__.py` needed — Python 3 supports namespace packages
  (implicit packages without `__init__.py`).
  
- Both commands must be run with venv activated.

## Analogy
Like a hotel room number. The building (`/hotel/`) is the same for everyone, but the room number (`{room_number}`) tells staff exactly which room to go to. `/hotel/305` means "go to room 305" — not the whole hotel, not a random room, that one specific room.er(123); // same idea as /users/123
```