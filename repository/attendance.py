
from Database.conect import cur, conn


def get_today_attendance(employee_id, today):

    cur.execute("""
        SELECT *
        FROM attendance
        WHERE employee_id = %s
        AND attendance_date = %s
    """, (employee_id, today))

    return cur.fetchone()


def create_attendance(employee_id, today, checkin):

    try:
        cur.execute("""
            INSERT INTO attendance (
                employee_id,
                attendance_date,
                status,
                checkin
            )
            VALUES (%s, %s, %s, %s)
        """, (
            employee_id,
            today,
            "Checked In",
            checkin
        ))

        conn.commit()

    except Exception:
        conn.rollback()
        raise


def update_attendance(employee_id, today, record):

    try:
        cur.execute("""
            UPDATE attendance
            SET
                status = %s,
                checkin = %s,
                checkout = %s,
                break_starts = %s,
                break_resumes = %s,
                break_duration = %s,
                working_time = %s
            WHERE employee_id = %s
            AND attendance_date = %s
        """, (
            record["status"],
            record["checkin"],
            record["checkout"],
            record["break_starts"],
            record["break_resumes"],
            record["break_duration"],
            record["working_time"],
            employee_id,
            today
        ))

        conn.commit()

    except Exception:
        conn.rollback()
        raise


def get_employee_attendance(employee_id, today=None):

    if today is not None:

        cur.execute("""
            SELECT *
            FROM attendance
            WHERE employee_id = %s
            AND attendance_date = %s
        """, (employee_id, today))

        return cur.fetchone()

    cur.execute("""
        SELECT *
        FROM attendance
        WHERE employee_id = %s
        ORDER BY attendance_date DESC
    """, (employee_id,))

    return cur.fetchall()
