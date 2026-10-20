import csv
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent.parent
    records_file = project_root / "data" / "completion_reports.csv"

    if not records_file.exists():
        print("No report records found.")
        return

    batch_name = input("Enter the submitted batch name: ").strip()

    if not batch_name:
        print("Please provide a batch name.")
        return

    # Read the records into a list.
    with records_file.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        records = list(reader)

    found = False

    for record in records:
        if record["batch_name"].strip().lower() == batch_name.lower():
            if record["status"] == "Submitted":
                print("This report is already marked as Submitted.")
                return

            record["status"] = "Submitted"
            found = True
            break

    if not found:
        print("Batch not found. No records were changed.")
        return

    # Save the records with the updated status.
    with records_file.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Report for {batch_name} marked as Submitted.")


if __name__ == "__main__":
    main()