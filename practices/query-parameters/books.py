from fastapi import FastAPI

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


## query parameters
@app.get("/books/")
async def read_category_by_query(category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category', '').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


## path and query parameter
@app.get("/books/{book_author}")
async def read_author_category_by_book(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author', '').casefold() == book_author.casefold() and \
            book.get('category', '').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return