

import csv
import os

FILE_NAME = 'expenses.csv'

def initialize_file():

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'amount', 'note'])

def add_expense():

    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, Utilities): ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid numeric value for the amount.")

    note = input("Enter a note (optional): ")

    # Append the new record to the CSV file
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")

def view_expenses():

    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded yet.")
        return

    total = 0.0
    print("\n--- All Expenses ---")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 4:
                date, category, amount_str, note = row
                try:
                    amount = float(amount_str)
                    total += amount
                    print(f"Date: {date} | Category: {category} | Amount: ${amount:.2f} | Note: {note}")
                except ValueError:
                    continue

    print("-" * 30)
    print(f"Total Amount Spent: ${total:.2f}")

def category_summary():

    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded yet.")
        return

    summary = {}
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 4:
                _, category, amount_str, _ = row
                try:
                    amount = float(amount_str)
                    if category in summary:
                        summary[category] += amount
                    else:
                        summary[category] = amount
                except ValueError:
                    continue

    print("\n--- Category-wise Spending Summary ---")
    if not summary:
        print("No valid expense data found to summarize.")
    else:
        for cat, total in summary.items():
            print(f"{cat}: ${total:.2f}")

def main():

    initialize_file()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
