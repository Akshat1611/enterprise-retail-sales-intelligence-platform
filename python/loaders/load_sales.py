import pandas as pd
from psycopg2.extras import execute_values

from python.database.db_connection import get_connection

INPUT_FILE = "data/raw/sales.csv"

def load_sales_csv():
    sales_df = pd.read_csv(INPUT_FILE)
    return sales_df

def load_sales_to_db(sales_df):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO fact_sales
        (
            customer_id,
            product_id,
            store_id,
            promotion_id,
            date_id,
            quantity,
            unit_price,
            discount,
            sales_amount,
            cost_price,
            profit,
            payment_method,
            order_status
        )
        VALUES %s
    """

    data = []
    for _, row in sales_df.iterrows():
        promotion_id = None
        if not pd.isna(row["promotion_id"]):
            promotion_id = int(row["promotion_id"])
        data.append(
            (
                int(row["customer_id"]),
                int(row["product_id"]),
                int(row["store_id"]),
                promotion_id,
                int(row["date_id"]),
                int(row["quantity"]),
                float(row["unit_price"]),
                float(row["discount"]),
                float(row["sales_amount"]),
                float(row["cost_price"]),
                float(row["profit"]),
                row["payment_method"],
                row["order_status"]
            )
        )
    execute_values(
        cursor,
        query,
        data
    )
    conn.commit()
    print(f"\n✅ {len(data):,} sales inserted successfully!")
    cursor.close()
    conn.close()

def main():
    print("\n========== LOADING SALES ==========\n")
    sales_df = load_sales_csv()
    print(f"Rows Found : {len(sales_df):,}")
    load_sales_to_db(sales_df)
    print("\n========== LOAD COMPLETED ==========\n")

if __name__ == "__main__":
    main()