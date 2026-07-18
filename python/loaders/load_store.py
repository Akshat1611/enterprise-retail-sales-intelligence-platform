import pandas as pd
from psycopg2.extras import execute_values

from python.database.db_connection import get_connection


def load_store(csv_path):

    df = pd.read_csv(csv_path)

    records = list(df.itertuples(index=False, name=None))

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO dim_store
    (
        store_name,
        city,
        state,
        region,
        manager_name
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

    print(f"✅ {len(records)} Stores Inserted")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_store("data/raw/stores.csv")