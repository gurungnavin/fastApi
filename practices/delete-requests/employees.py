from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "Employee One", "email": "employee1@example.com", "department": "Engineering"},
    {"id": 2, "name": "Employee Two", "email": "employee2@example.com", "department": "Sales"},
    {"id": 3, "name": "Employee Three", "email": "employee3@example.com", "department": "HR"},
]



@app.get("/employees")
async def get_all_employees():
    return employees


@app.delete("/employee/delete-employee/{name}")
async def delete_employee(name : str):
    for i in range(len(employees)):
        if employees[i].get('name', '').casefold() == name.casefold():
            employees.pop(i)
            return {"message": "Employee deleted"}
    return{"error": "Employee not found"}