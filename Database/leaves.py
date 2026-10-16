from conect import cur ,conn


q="""CREATE TABLE IF NOT EXISTS leaves (
    employee_id VARCHAR(36) PRIMARY KEY
        REFERENCES "register"(employee_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason TEXT,
    total_leave_days INT NOT NULL
)"""
cur.execute(q)
print("Table created successfully")
conn.commit()