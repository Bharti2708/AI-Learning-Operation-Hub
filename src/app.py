from chat_app import main as ask_sop_question
from report_tracker import main as register_batch
from check_reports import main as check_reports
from mark_submitted import main as mark_submitted


def main():
    while True:
        print("\nAI LEARNING OPERATIONS HUB")
        print("1. Open Trainer SOP Assistant")
        print("2. Register a completed batch")
        print("3. Preview report reminders")
        print("4. Mark a report as Submitted")
        print("5. Exit")

        choice = input("\nChoose an option (1–5): ").strip()

        if choice == "1":
            ask_sop_question()

        elif choice == "2":
            register_batch()

        elif choice == "3":
            check_reports()

        elif choice == "4":
            mark_submitted()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()