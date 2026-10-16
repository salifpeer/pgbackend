from Database.conect import cur, conn



def load_employees():
    cur.execute("SELECT * FROM register")
    return cur.fetchall()


def get_employee(employee_id):
    cur.execute(
        "SELECT * FROM register WHERE employee_id = %s",
        (employee_id,)
    )
    return cur.fetchone()


def get_employee_by_email(email):
    cur.execute(
        "SELECT * FROM register WHERE email = %s",
        (email,)
    )
    return cur.fetchone()


def save_employee(employee):
    try:
        cur.execute(
            """
            INSERT INTO register (
                employee_id,
                full_name,
                email,
                date_of_birth,
                gender,
                marital_status,
                nationality,
                mobile,
                alternate_mobile,
                present_address,
                password
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                employee["employee_id"],
                employee["full_name"],
                employee["email"],
                employee["date_of_birth"],
                employee["gender"],
                employee["marital_status"],
                employee["nationality"],
                employee["mobile"],
                employee["alternate_mobile"],
                employee["present_address"],
                employee["password"]
            )
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise