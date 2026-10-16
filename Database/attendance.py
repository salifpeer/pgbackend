from conect import cur ,conn

q="""CREATE TABLE IF NOT EXISTS attendance (
    employee_id VARCHAR(100) NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    checkin TIMESTAMP,
    checkout TIMESTAMP,
    break_starts TIMESTAMP[] DEFAULT '{}',
    break_resumes TIMESTAMP[] DEFAULT '{}',
    break_duration INTERVAL DEFAULT INTERVAL '0',
    working_time INTERVAL,

    PRIMARY KEY (employee_id, attendance_date),

    FOREIGN KEY (employee_id)
        REFERENCES register(employee_id)
)"""
cur.execute(q)
print("Table created successfully")
conn.commit()