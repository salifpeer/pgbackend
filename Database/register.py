from conect import cur ,conn

from conect import cur ,conn

q="""CREATE TABLE IF NOT EXISTS register(
    employee_id       VARCHAR(100) PRIMARY KEY,
    full_name         VARCHAR(100),
    email             VARCHAR(254) ,
    date_of_birth     DATE,
    gender            VARCHAR(20),
    marital_status    VARCHAR(20),
    nationality       VARCHAR(50),
    mobile            VARCHAR(20),
    alternate_mobile  VARCHAR(20),
    present_address   TEXT,
    password          VARCHAR(255)
)"""

cur.execute(q)
print("Table created successfully")


conn.commit()