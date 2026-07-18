import pandas as pd
from psycopg2.extras import execute_values

from python.database.db_connection import get_connection


def load_dates(csv_path):

    df = pd.read_csv(csv_path)

    records = list(df.itertuples(index=False, name=None))

    conn = get_connection()

    if conn is None:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO dim_date
    (
        full_date,
        day,
        month,
        month_name,
        quarter,
        year,
        weekday,
        is_weekend
    )
    VALUES %s
    """

    execute_values(
        cursor,
        query,
        records,
        page_size=1000
    )

    conn.commit()

    print(f"✅ {len(records)} dates inserted successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_dates("data/raw/dates.csv")