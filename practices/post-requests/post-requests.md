# POST Request

## Introduction
A POST request is an HTTP method used to **send data to the server to create a new resource** (e.g. a new user, book, order). Unlike GET, the data travels in the **request body**, not the URL.

## Syntax
```python
@app.post("/path")
async def function_name(payload: SomeModel):
    return payload
```

## Why
- Body can hold more/structured data than a URL can
- Each call creates a new resource (unlike GET, which just reads)
- Keeps data out of the URL (not logged, not cached)s

## How
```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str

@app.post("/books/create_book")
async def create_book(new_book: Book):
    BOOKS.append(new_book)
    return new_book
```
- `Book` (Pydantic model) → defines and validates the expected JSON shape
- Client sends `{"title": ..., "author": ...}` in the body
- FastAPI parses, validates, and converts it into a `Book` instance automatically
- Invalid/missing fields → 422 validation error

## When
Use POST when the client is **creating** something new:
- `/books/create_book`
- `/users/register`
- `/orders`

Not for fetching (`GET`), not for identifying an existing resource by ID in the URL (`path parameters` handle that).

## Analogy
Like filling out a form and handing it to a clerk to open a new file. You (client) fill in the details (body), hand it over (POST), and the clerk creates a brand-new record from it — you're not asking to see an existing file, you're creating one.