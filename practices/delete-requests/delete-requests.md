# DELETE Request

## Introduction
A DELETE request is an HTTP method used to **remove an existing resource**. It identifies the resource via the URL (path param) — no request body needed.

## Syntax
```python
@app.delete("/path/{id}")
async def function_name(id: int):
    ...
```

## Why
- Removes a resource instead of creating/reading/updating it
- Idempotent — deleting the same resource twice ends in the same state (gone)
- No body needed — URL alone identifies the target, matching REST convention

## How
```python
@app.delete("/employee/delete_employee/{name}")
async def delete_employee(name: str):
    for i in range(len(employees)):
        if employees[i].get('name').casefold() == name.casefold():
            employees.pop(i)
            return {"message": "Employee deleted"}
    return {"error": "Employee not found"}
```
- `name` (path param) → identifies which resource to delete
- Loop through the in-memory list to find a match (manual lookup, no DB here)
- `casefold()` → case-insensitive comparison
- Return a confirmation message after deletion (or an error if not found)

## When
Use DELETE when the client is **removing** an existing resource:
- `/employee/delete_employee/{name}`
- `/books/{id}`
- `/orders/{id}`

Not for creating (`POST`), updating (`PUT`), or reading (`GET`).

## Analogy
Like shredding a specific file by its label. You point to which one (via the URL), it's gone — do it twice, nothing changes the second time, it was already gone.