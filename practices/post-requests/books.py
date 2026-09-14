from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
    {"title": "Title Seven", "author": "Author Two", "category": "history"},
    {"title": "Title Eight", "author": "Author Three", "category": "science"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

class Book(BaseModel):
    title : str
    author : str
    category: str

@app.post("/books/create_book")
async def create_book(new_book: Book = Body()):
    BOOKS.append(new_book.dict())
    return new_book