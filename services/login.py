
from fastapi import HTTPException

from repository.login import get_employee_by_email
from auth.auth import create_token


def login_user(email, password):

    
    employee = get_employee_by_email(email)

    if employee is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    
    if employee["password"] != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    
    token = create_token(employee["email"])

    return {
        "message": "Login successful",
        "status_code": 200,
        "access_token": token,
        "token_type": "bearer",
        "employee_id": employee["employee_id"],
        "full_name": employee["full_name"],
        "email": employee["email"],
        "date_of_birth": str(employee["date_of_birth"]) if employee["date_of_birth"] else None,
        "gender": employee["gender"],
        "marital_status": employee["marital_status"],
        "nationality": employee["nationality"],
        "mobile": employee["mobile"]
    }
