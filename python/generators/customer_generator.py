import random
from datetime import date

import pandas as pd
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker("en_IN")

# Customer segments
SEGMENTS = ["Regular", "Premium", "VIP"]


def generate_customer():
    """Generate a single customer record."""

    gender = random.choice(["Male", "Female"])

    return {
        "customer_name": fake.name_male() if gender == "Male" else fake.name_female(),
        "gender": gender,
        "age": random.randint(18, 70),
        "city": fake.city(),
        "state": fake.state(),
        "country": "India",
        "income": round(random.uniform(200000, 2500000), 2),
        "customer_segment": random.choice(SEGMENTS),
        "join_date": fake.date_between(
            start_date=date(2019, 1, 1),
            end_date=date(2025, 12, 31)
        )
    }


def generate_customers(total_records=50000):
    """Generate multiple customer records."""

    customers = []

    for _ in range(total_records):
        customers.append(generate_customer())

    return pd.DataFrame(customers)


def main():
    print("Generating customer data...")

    df = generate_customers(50000)

    print(df.head())

    output_path = "data/raw/customers.csv"

    df.to_csv(output_path, index=False)

    print(f"\n✅ {len(df)} customer records generated successfully!")
    print(f"📁 File saved at: {output_path}")


if __name__ == "__main__":
    main()