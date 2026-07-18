import pandas as pd
from psycopg2.extras import execute_values

from python.database.db_connection import get_connection


def load_promotion(csv_path):

    df = pd.read_csv(csv_path)

    records = list(df.itertuples(index=False, name=None))

    conn = get_connection()

    cursor = conn.cursor()

    query = """
INSERT INTO dim_promotion
(
    campaign_name,
    discount_percent,
    start_date,
    end_date
)
VALUES %s
"""

    execute_values(cursor, query, records)

    conn.commit()

    print(f"✅ {len(records)} Promotions Inserted")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_promotion("data/raw/promotions.csv")