import pandas as pd


def generate_dates():
    """
    Generate a complete date dimension from 2020-01-01 to 2025-12-31.
    """

    dates = pd.date_range(
        start="2020-01-01",
        end="2025-12-31",
        freq="D"
    )

    df = pd.DataFrame({
        "full_date": dates,
        "day": dates.day,
        "month": dates.month,
        "month_name": dates.strftime("%B"),
        "quarter": dates.quarter,
        "year": dates.year,
        "weekday": dates.day_name(),
        "is_weekend": dates.weekday >= 5
    })

    return df


def main():

    print("Generating Date Dimension...")

    df = generate_dates()

    print(df.head())

    output_path = "data/raw/dates.csv"

    df.to_csv(output_path, index=False)

    print(f"\n✅ {len(df)} dates generated successfully!")
    print(f"📁 Saved to: {output_path}")


if __name__ == "__main__":
    main()