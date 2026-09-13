# Query Parameters

## Introduction
A query parameter is an optional key-value pair added to the end of a URL, after a `?`, used to filter, search, or customize results — not to identify one specific resource.

## Why
- Lets you search/filter a collection without hardcoding every possible route
- Supports partial or flexible matching (unlike path parameters, which require exact matches)
- Optional by nature — a route can define several query parameters, and the caller only sends the ones they need
- Keeps result sets flexible: return one match, many matches, or none

## Syntax

@app.get("/route")
async def function_name(param_name: type):
    return {"param_name": param_name}

Multiple query parameters:

@app.get("/books/")
async def read_books(category: str, author: str):
    return {"category": category, "author": author}

Called as:
/books/?category=science&author=author+one

## How

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category', '').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

- `/books/?category=science` → `category = "science"`
- Loops through the collection, returns all matches (not just one)
- Missing key handled safely with `.get('category', '')` — avoids crashing on `None`

## When
Use query parameters when:
- Searching/filtering a collection (`?category=science`)
- The match doesn't need to be exact (`?title=to kill`)
- The parameter is optional, or there could be multiple valid combinations

Not for identifying one specific resource by ID — that's what path parameters are for.

## Path + Query Together
You can combine both in a single route — path parameter for a specific field, query parameter for an additional filter:

@app.get("/books/{book_author}")
async def read_author_category_by_book(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author', '').casefold() == book_author.casefold() and \
           book.get('category', '').casefold() ==