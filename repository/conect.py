
import psycopg2
from psycopg2.extras import RealDictCursor



DATABASE_URL = "postgresql://root:561nv8PfP9gnzEKcPQMzXIAHodCp6sqt@dpg-db8ugvs9v7es73du76o0-a.oregon-postgres.render.com/tms_89t2"

try:
    conn = psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor,
        sslmode="require"
    )

    cur = conn.cursor()

    print("Connected to Render PostgreSQL successfully!")

except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
    raise
