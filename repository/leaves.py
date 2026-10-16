from Database.conect import cur ,conn

def create_leave(leave):
     cur.execute("""
            INSERT INTO leaves (
                employee_id,
                start_date,
                end_date,
                reason,
                total_leave_days
                
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            leave["employee_id"],
            leave["start_date"],
            leave["end_date"],
            leave["reason"],
            leave["total_leave_days"]
        ))

     conn.commit()

    



def get_employee_leaves(employee_id):


        

        cur.execute("""
            SELECT *
            FROM leaves
            WHERE employee_id = %s
            ORDER BY start_date DESC
        """, (employee_id,))

        return [dict(row) for row in cur.fetchall()]

    
