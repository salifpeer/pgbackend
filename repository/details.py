from Database.conect import cur, conn

def get_employee_details(employee_id):
    cur.execute(
        """
        SELECT *
        FROM register
        WHERE employee_id = %s
        """,
        (employee_id,)
    )
    return cur.fetchone()
