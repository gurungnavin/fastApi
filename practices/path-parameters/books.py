from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Title one", "author": "J.D. Salinger", "category": "Fiction"},
    {"title": "Title two", "author": "Harper Lee", "category": "historical fiction"},
    {"title": "Title three", "author": "George Orwell", "category": "Dystopian"},
    {"title": "Title four", "author": "Jane Austen", "category": "Romance"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


## path parameters
@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book