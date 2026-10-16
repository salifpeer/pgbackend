
from uuid import uuid4
from fastapi import HTTPException
from repository.Register import get_employee_by_email, save_employee

def register_employee_service(employee):

    if hasattr(employee, "model_dump"):
        employee_data = employee.model_dump(mode="json")
    else:
        employee_data = employee.copy()

    employee_data["email"] = employee_data["email"].strip().lower()

    existing_employee = get_employee_by_email(
        employee_data["email"]
    )

    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="An account with this email address already exists."
        )

    employee_data["employee_id"] = str(uuid4())

    try:
        save_employee(employee_data)


    except Exception as e:
        if "unique" in str(e).lower():
            raise HTTPException(
                status_code=400,
                detail="An account with this email address already exists."
            )
        raise

    return {
        "message": "Employee registered successfully",
        "employee": employee_data
    }
