
from datetime import datetime, date, timedelta

from repository.attendance import (
    get_today_attendance,
    create_attendance,
    update_attendance,
    get_employee_attendance
)


TIME_FORMAT = "%d-%b-%Y %I:%M:%S %p"


def get_current_time():
    return datetime.now()


def get_today():
    return date.today()


def format_time(value):
    if value is None:
        return "-"
    return value.strftime(TIME_FORMAT)


def format_duration(value):
    if not value:
        return "0:00:00"

    total_seconds = int(value.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours}:{minutes:02}:{seconds:02}"


def get_employee(employee_id):

    today = get_today()
    employee = get_today_attendance(employee_id, today)

    if employee is None:
        return {
            "status": "Not Checked In",
            "checkin": None,
            "checkout": None,
            "break_starts": [],
            "break_resumes": [],
            "break_duration": timedelta(),
            "working_time": None
        }

    return dict(employee)


def response(message, employee):

    return {
        "message": message,
        "status": employee["status"],
        "checkin_time": format_time(employee["checkin"]),
        "checkout_time": format_time(employee["checkout"]),
        "break_time": format_duration(employee["break_duration"]),
        "working_time": format_duration(employee["working_time"])
            if employee["working_time"] is not None else "-"
    }


def save_employee(employee_id, employee):

    update_attendance(employee_id, get_today(), employee)


# CHECK IN

def checkin(employee_id):

    today = get_today()
    employee = get_employee_attendance(employee_id, today)

    if employee:
        return response("Already checked in", dict(employee))

    now = get_current_time()

    create_attendance(employee_id, today, now)

    employee = get_employee_attendance(employee_id, today)

    return response("Checked in successfully", dict(employee))


# START BREAK

def start_break(employee_id):

    employee = get_employee(employee_id)

    if not employee["checkin"]:
        return response("Please check in first", employee)

    if employee["checkout"]:
        return response("Already checked out", employee)

    if len(employee["break_starts"]) > len(employee["break_resumes"]):
        return response("Already on break", employee)

    employee["break_starts"].append(get_current_time())
    employee["status"] = "On Break"

    save_employee(employee_id, employee)

    return response("Break started", employee)


# RESUME BREAK

def resume_break(employee_id):

    employee = get_employee(employee_id)

    if not employee["break_starts"] or (
        len(employee["break_starts"]) == len(employee["break_resumes"])
    ):
        return response("You are not on break", employee)

    now = get_current_time()
    employee["break_resumes"].append(now)

    start = employee["break_starts"][-1]
    employee["break_duration"] += now - start
    employee["status"] = "Checked In"

    save_employee(employee_id, employee)

    return response("Break resumed successfully", employee)


# CHECK OUT

def checkout(employee_id):

    employee = get_employee(employee_id)

    if not employee["checkin"]:
        return response("Please check in first", employee)

    if employee["checkout"]:
        return response("Already checked out", employee)

    if len(employee["break_starts"]) > len(employee["break_resumes"]):
        return response("Please resume your break first", employee)

    now = get_current_time()

    employee["checkout"] = now
    employee["working_time"] = (
        now - employee["checkin"] - employee["break_duration"]
    )
    employee["status"] = "Checked Out"

    save_employee(employee_id, employee)

    return response("Checked out successfully", employee)


# GET ATTENDANCE

def get_attendance(employee_id):

    rows = get_employee_attendance(employee_id)

    result = {}

    for row in rows:
        attendance_date = row["attendance_date"].strftime("%d-%b-%Y")

        result[attendance_date] = {
            "status": row["status"],
            "checkin": format_time(row["checkin"]),
            "checkout": format_time(row["checkout"]),
            "break_starts": [
                format_time(value) for value in (row["break_starts"] or [])
            ],
            "break_resumes": [
                format_time(value) for value in (row["break_resumes"] or [])
            ],
            "break_duration": format_duration(row["break_duration"]),
            "working_time": (
                format_duration(row["working_time"])
                if row["working_time"] is not None else ""
            )
        }

    return result
