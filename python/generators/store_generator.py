import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

INDIAN_STORES = {
    "North": {
        "Delhi": "Delhi",
        "Lucknow": "Uttar Pradesh",
        "Jaipur": "Rajasthan",
        "Chandigarh": "Punjab"
    },
    "South": {
        "Hyderabad": "Telangana",
        "Bengaluru": "Karnataka",
        "Chennai": "Tamil Nadu",
        "Kochi": "Kerala"
    },
    "West": {
        "Mumbai": "Maharashtra",
        "Pune": "Maharashtra",
        "Ahmedabad": "Gujarat",
        "Surat": "Gujarat"
    },
    "East": {
        "Kolkata": "West Bengal",
        "Bhubaneswar": "Odisha",
        "Patna": "Bihar",
        "Ranchi": "Jharkhand"
    }
}


def generate_store():

    region = random.choice(list(INDIAN_STORES.keys()))

    city = random.choice(list(INDIAN_STORES[region].keys()))

    state = INDIAN_STORES[region][city]

    return {
        "store_name": f"{city} {random.choice(['Mega Store','Super Store','Retail Hub','Express'])}",
        "city": city,
        "state": state,
        "region": region,
        "manager_name": fake.name()
    }


def generate_stores(total=500):

    stores = []

    for _ in range(total):
        stores.append(generate_store())

    return pd.DataFrame(stores)


def main():

    df = generate_stores()

    print(df.head())

    df.to_csv(
        "data/raw/stores.csv",
        index=False
    )

    print(f"\n✅ {len(df)} Stores Generated")


if __name__ == "__main__":
    main()