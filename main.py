import os

import matplotlib.pyplot as plt
import pandas as pd


def create_workforce_pie_chart(data, date):
    zone_allocation = (
        data[data["Timestamp"].dt.date == date]
        .groupby("Zone Name")["Workers Assigned"]
        .mean()
    )

    total_workers = zone_allocation.sum()
    percentages = (zone_allocation / total_workers * 100).round(1)

    plt.figure(figsize=(10, 8))
    plt.pie(
        percentages,
        labels=[f"{zone}\n{pct}%" for zone, pct in percentages.items()],
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title(f"Workforce Allocation by Zone - {date}")

    os.makedirs("output", exist_ok=True)

    output_file = f"output/{date}.png"
    plt.savefig(output_file)
    plt.close()

    return output_file


def process_workforce_data(csv_file):
    df = pd.read_csv(csv_file)

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    unique_dates = df["Timestamp"].dt.date.unique()

    output_files = []
    for date in unique_dates:
        output_file = create_workforce_pie_chart(df, date)
        output_files.append(output_file)
        print(f"Created chart for {date}: {output_file}")


def main():
    csv_file = "data/data.csv"
    process_workforce_data(csv_file)


if __name__ == "__main__":
    main()
