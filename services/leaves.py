
from datetime import datetime

from repository.leaves import create_leave, get_employee_leaves


def apply_leave(employee_id, start_date, end_date, reason):

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if end < start:
        return {
            "message": "Ending date cannot be before starting date"
        }

    total_leave_days = (end - start).days + 1

    leave = {
        "employee_id": employee_id,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "total_leave_days": total_leave_days,
        
    }

    create_leave(leave)

    return {
        "message": "Leave applied successfully",
        "employee_id": employee_id,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "total_leave_days": total_leave_days
    }


def get_leaves(employee_id):

    return get_employee_leaves(employee_id)
