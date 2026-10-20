import csv
from pathlib import Path

from datetime import datetime, timedelta


def calculate_due_date(completion_date):
    """Calculate a deadline seven calendar days after completion."""
    return completion_date + timedelta(days=7)


def main():
    print("\nCompletion Report Tracker")

    batch_name = input("Enter the batch name: ").strip()
    date_text = input("Batch completion date (YYYY-MM-DD): ").strip()

    if not batch_name:
        print("Please provide a batch name.")
        return

    try:
        completion_date = datetime.strptime(
            date_text, "%Y-%m-%d"
        ).date()
    except ValueError:
        print("Please enter a valid date in YYYY-MM-DD format.")
        return

    due_date = calculate_due_date(completion_date)

    print(f"\nBatch: {batch_name}")
    print(f"Completion date: {completion_date}")
    print(f"Report due date: {due_date}")

    # Save records in the project's data folder.
    project_root = Path(__file__).resolve().parent.parent
    records_file = project_root / "data" / "completion_reports.csv"
    records_file.parent.mkdir(parents=True, exist_ok=True)

    needs_header = (
        not records_file.exists()
        or records_file.stat().st_size == 0
    )

        # Check whether this batch is already recorded.
    if records_file.exists():
        with records_file.open(
            "r", newline="", encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                saved_name = row["batch_name"].strip().lower()

                if saved_name == batch_name.lower():
                    print("\nThis batch is already recorded.")
                    return
                
    with records_file.open(
        "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        if needs_header:
            writer.writerow([
                "batch_name",
                "completion_date",
                "due_date",
                "status",
            ])

        writer.writerow([
            batch_name,
            completion_date,
            due_date,
            "Pending",
        ])

    print("\nRecord saved.")

if __name__ == "__main__":
    main()