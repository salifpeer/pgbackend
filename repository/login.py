
from Database.conect import cur, conn


def get_employee_by_email(email):
    cur.execute(
        """
        SELECT *
        FROM register
        WHERE LOWER(email) = %s
        """,
        (email.strip().lower(),)
    )

    return cur.fetchone()


def get_employee_by_id(employee_id):
    cur.execute(
        """
        SELECT *
        FROM register
        WHERE employee_id = %s
        """,
        (employee_id,)
    )

    return cur.fetchone()
