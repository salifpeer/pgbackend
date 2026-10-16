from conect import cur

q="""CREATE TABLE IF NOT EXISTS user (
    employee_id       VARCHAR(36) PRIMARY KEY,
    full_name         VARCHAR(100),
    email             VARCHAR(254),
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
cur.commit()