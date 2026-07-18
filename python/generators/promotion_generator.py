import random
from datetime import date

import pandas as pd

PROMOTIONS = [
    "Diwali Sale",
    "New Year Sale",
    "Republic Day Sale",
    "Independence Day Sale",
    "Summer Sale",
    "Winter Sale",
    "Monsoon Offer",
    "Festive Bonanza",
    "Weekend Special",
    "End of Season Sale",
    "Mega Electronics Sale",
    "Fashion Fiesta",
    "Big Grocery Days",
    "Flash Sale",
    "Clearance Sale"
]


def generate_promotion():
    start_year = random.randint(2020, 2025)
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)

    start_date = date(start_year, start_month, start_day)

    duration = random.randint(5, 30)

    end_date = start_date + pd.Timedelta(days=duration)

    return {
        "promotion_name": random.choice(PROMOTIONS),
        "discount_percentage": random.choice([5, 10, 15, 20, 25, 30, 40, 50]),
        "start_date": start_date,
        "end_date": end_date
    }


def generate_promotions(total=100):
    promotions = []

    for _ in range(total):
        promotions.append(generate_promotion())

    return pd.DataFrame(promotions)


def main():
    df = generate_promotions()

    print(df.head())

    df.to_csv(
        "data/raw/promotions.csv",
        index=False
    )

    print(f"\n✅ {len(df)} Promotions Generated")


if __name__ == "__main__":
    main()