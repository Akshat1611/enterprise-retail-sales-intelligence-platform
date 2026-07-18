import random
import pandas as pd

# Product catalog
PRODUCT_CATALOG = {
    "Electronics": {
        "brands": ["Samsung", "Apple", "Sony", "LG", "HP", "Dell", "Lenovo"],
        "products": ["Laptop", "Smartphone", "Monitor", "Keyboard", "Mouse", "Headphones", "Tablet"]
    },
    "Clothing": {
        "brands": ["Nike", "Adidas", "Puma", "Levis", "Zara", "H&M"],
        "products": ["T-Shirt", "Jeans", "Jacket", "Shoes", "Cap", "Shorts"]
    },
    "Grocery": {
        "brands": ["Amul", "Nestle", "Britannia", "Tata", "Fortune"],
        "products": ["Milk", "Bread", "Butter", "Rice", "Sugar", "Tea"]
    },
    "Home & Kitchen": {
        "brands": ["Prestige", "Philips", "Havells", "Bajaj"],
        "products": ["Mixer", "Cooker", "Fan", "Iron", "Toaster"]
    },
    "Beauty": {
        "brands": ["Lakme", "Nivea", "Dove", "Loreal"],
        "products": ["Shampoo", "Face Wash", "Soap", "Cream", "Perfume"]
    },
    "Sports": {
        "brands": ["Yonex", "SG", "Cosco", "Nivia"],
        "products": ["Football", "Cricket Bat", "Badminton Racket", "Basketball"]
    },
    "Books": {
        "brands": ["Penguin", "Pearson", "McGraw Hill"],
        "products": ["Novel", "Data Science", "Python Programming", "SQL Guide"]
    }
}

SUPPLIERS = [
    "ABC Traders",
    "Global Retail Supply",
    "Tech Distributors Pvt Ltd",
    "Prime Wholesale",
    "National Suppliers",
    "Retail Hub India"
]


def generate_product():
    category = random.choice(list(PRODUCT_CATALOG.keys()))

    brand = random.choice(PRODUCT_CATALOG[category]["brands"])
    product = random.choice(PRODUCT_CATALOG[category]["products"])

    cost_price = round(random.uniform(100, 50000), 2)

    margin = random.uniform(1.10, 1.50)

    selling_price = round(cost_price * margin, 2)

    return {
        "product_name": f"{brand} {product}",
        "category": category,
        "brand": brand,
        "supplier": random.choice(SUPPLIERS),
        "cost_price": cost_price,
        "selling_price": selling_price
    }


def generate_products(total_records=5000):
    products = []

    for _ in range(total_records):
        products.append(generate_product())

    return pd.DataFrame(products)


def main():
    print("Generating products...")

    df = generate_products(5000)

    print(df.head())

    output_path = "data/raw/products.csv"

    df.to_csv(output_path, index=False)

    print(f"\n✅ {len(df)} products generated successfully!")
    print(f"📁 File saved at: {output_path}")


if __name__ == "__main__":
    main()