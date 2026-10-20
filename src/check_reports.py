import csv
from datetime import date
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent.parent
    records_file = project_root / "data" / "completion_reports.csv"

    if not records_file.exists():
        print("No report records found.")
        return

    today = date.today()
    reminder_count = 0

    print(f"\nReport check for {today}")

    with records_file.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            due_date = date.fromisoformat(row["due_date"])

            if row["status"] == "Pending" and due_date <= today:
                print(
                    f"\nReminder preview: The completion report "
                    f"for {row['batch_name']} is pending. "
                    f"Its due date is {due_date}."
                )
                reminder_count += 1

    if reminder_count == 0:
        print("No pending reports are due today or overdue.")


if __name__ == "__main__":
    main()