import random
import pandas as pd
from python.database.db_connection import get_connection

NUM_SALES = 10000
OUTPUT_FILE = "data/raw/sales.csv"
RANDOM_SEED = 42

def load_dimension_tables():
    conn = get_connection()
    tables = {
        "customers": pd.read_sql("SELECT * FROM dim_customer", conn),
        "products": pd.read_sql("SELECT * FROM dim_product", conn),
        "stores": pd.read_sql("SELECT * FROM dim_store", conn),
        "promotions": pd.read_sql("SELECT * FROM dim_promotion", conn),
        "dates": pd.read_sql("SELECT * FROM dim_date", conn),
    }
    conn.close()
    return tables

def get_random_row(df):
    return df.sample(1).iloc[0]

def choose_product(products, customer_segment):
    if customer_segment == "Regular":

        preferred = [
            "Grocery",
            "Books",
            "Beauty"
        ]
    elif customer_segment == "Premium":

        preferred = [
            "Clothing",
            "Home",
            "Sports"
        ]
    else:
        preferred = [
            "Electronics",
            "Sports",
            "Clothing"
        ]
    filtered = products[
        products["category"].isin(preferred)
    ]
    if filtered.empty:
        return get_random_row(products)
    return get_random_row(filtered)

def choose_quantity(category):
    quantity_rules = {
        "Electronics": (1, 1),
        "Sports": (1, 2),
        "Home": (1, 2),
        "Clothing": (1, 3),
        "Books": (1, 3),
        "Beauty": (1, 4),
        "Grocery": (1, 8)
    }
    low, high = quantity_rules.get(category, (1, 2))
    return random.randint(low, high)

def choose_promotion(promotions):
    use_promotion = random.choices(
        [True, False],
        weights=[40, 60]
    )[0]
    if not use_promotion:
        return None, 0
    promo = get_random_row(promotions)
    discount = promo["discount_percent"] / 100
    return promo, discount

def choose_payment_method():
    return random.choices(
        [
            "UPI",
            "Card",
            "Cash",
            "Net Banking"
        ],
        weights=[45, 30, 15, 10]
    )[0]

def choose_order_status():
    return random.choices(
        [
            "Completed",
            "Returned",
            "Cancelled"
        ],
        weights=[95, 3, 2]
    )[0]

def generate_single_sale(tables):
    customer = get_random_row(
        tables["customers"]
    )
    product = choose_product(
        tables["products"],
        customer["customer_segment"]
    )
    store = get_random_row(
        tables["stores"]
    )
    date = get_random_row(
        tables["dates"]
    )
    promotion, discount = choose_promotion(
        tables["promotions"]
    )
    quantity = choose_quantity(
        product["category"]
    )
    payment = choose_payment_method()
    status = choose_order_status()
    unit_price = product["selling_price"]
    cost_price = product["cost_price"]
    sales_amount = quantity * unit_price * (1 - discount)
    profit = sales_amount - (quantity * cost_price)
    sale = {
        "customer_id": customer["customer_id"],
        "customer_name": customer["customer_name"],
        "segment": customer["customer_segment"],
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "store_id": store["store_id"],
        "store_name": store["store_name"],
        "date_id": date["date_id"],
        "date": date["full_date"],
        "promotion_id": None if promotion is None else promotion["promotion_id"],
        "discount": round(discount, 2),
        "quantity": quantity,
        "unit_price": round(unit_price, 2),
        "sales_amount": round(sales_amount, 2),
        "cost_price": round(cost_price, 2),
        "profit": round(profit, 2),
        "payment_method": payment,
        "order_status": status
    }
    return sale

def main():
    random.seed(RANDOM_SEED)
    tables = load_dimension_tables()
    print("\nDIMENSION TABLES \n")
    for table_name, df in tables.items():
        print(f"{table_name:<12}: {len(df):,} rows")
    print("\nGENERATING SALES\n")
    sales_df = generate_sales_batch(
        tables,
        num_sales=NUM_SALES
    )
    sales_df.to_csv(
        OUTPUT_FILE,
        index=False
    )
    print("\nSales CSV created successfully.")
    print(f"Total Sales Generated: {len(sales_df):,}")
    print(f"Output File: {OUTPUT_FILE}")
    print("\nFirst 10000 sales\n")
    print(sales_df.head())

def generate_sales_batch(tables, num_sales):
    sales = []
    for _ in range(num_sales):
        sale = generate_single_sale(tables)
        sales.append(sale)
    sales_df = pd.DataFrame(sales)
    return sales_df

if __name__ == "__main__":
    main()