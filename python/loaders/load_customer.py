import pandas as pd
from psycopg2.extras import execute_values

from python.database.db_connection import get_connection


def load_customers(csv_path):
    """Load customer data from CSV into PostgreSQL."""

    # Read CSV
    df = pd.read_csv(csv_path)

    # Convert DataFrame to list of tuples
    records = list(df.itertuples(index=False, name=None))

    conn = get_connection()

    if conn is None:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO dim_customer (
        customer_name,
        gender,
        age,
        city,
        state,
        country,
        income,
        customer_segment,
        join_date
    )
    VALUES %s
    """

    execute_values(cursor, query, records, page_size=1000)

    conn.commit()

    print(f"✅ {len(records)} customers inserted successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_customers("data/raw/customers.csv")