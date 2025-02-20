import json
import os
from datetime import datetime

EXPENSE_FILE = "expenses.json"

# Load expenses from file (Handles empty or missing files)
def load_expenses():
    if os.path.exists(EXPENSE_FILE) and os.path.getsize(EXPENSE_FILE) > 0:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Generate a unique expense ID
def generate_expense_id(expenses):
    if not expenses:
        return 1
    return max(exp["id"] for exp in expenses) + 1

# Add an expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: ").strip() or "0")
        category = input("Enter expense category (Food, Travel, Shopping, etc.): ").strip().title()
        date = input("Enter date (YYYY-MM-DD) [Default: Today]: ").strip() or datetime.today().strftime('%Y-%m-%d')

        expenses = load_expenses()
        expense_id = generate_expense_id(expenses)
        expenses.append({"id": expense_id, "amount": amount, "category": category, "date": date})

        save_expenses(expenses)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number for the amount.")

# View expenses
def view_expenses(filter_by_category=None):
    expenses = load_expenses()
    if not expenses:
        print("❌ No expenses found!")
        return

    filtered_expenses = [exp for exp in expenses if not filter_by_category or exp["category"].lower() == filter_by_category.lower()]

    if not filtered_expenses:
        print(f"❌ No expenses found in category: {filter_by_category}")
        return

    print("\n📊 Your Expenses:")
    for exp in filtered_expenses:
        print(f"ID: {exp['id']} | Amount: ₹{exp['amount']} | Category: {exp['category']} | Date: {exp['date']}")

# Edit an expense
def edit_expense():
    expenses = load_expenses()
    if not expenses:
        print("❌ No expenses to edit!")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter Expense ID to edit: ").strip())
        for exp in expenses:
            if exp["id"] == expense_id:
                exp["amount"] = float(input(f"New Amount (Current: {exp['amount']}): ").strip() or exp["amount"])
                exp["category"] = input(f"New Category (Current: {exp['category']}): ").strip().title() or exp["category"]
                exp["date"] = input(f"New Date (Current: {exp['date']}): ").strip() or exp["date"]
                save_expenses(expenses)
                print("✅ Expense updated successfully!")
                return
        print("❌ Expense ID not found!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

# Delete an expense
def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("❌ No expenses to delete!")
        return

    view_expenses()
    try:
        expense_id = int(input("\nEnter Expense ID to delete: ").strip())

        new_expenses = [exp for exp in expenses if exp["id"] != expense_id]
        if len(new_expenses) == len(expenses):
            print("❌ Expense ID not found!")
            return
        
        save_expenses(new_expenses)
        print("✅ Expense deleted successfully!")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

# Filter expenses by category
def filter_by_category():
    category = input("Enter category to filter (Food, Travel, Shopping, etc.): ").strip().title()
    view_expenses(filter_by_category=category)

# Show monthly summary
def monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("❌ No expenses found!")
        return

    summary = {}
    for exp in expenses:
        month = exp["date"][:7]  # Extract YYYY-MM from date
        summary[month] = summary.get(month, 0) + exp["amount"]

    print("\n📆 Monthly Expense Summary:")
    for month, total in summary.items():
        print(f"{month}: ₹{total}")

# Main menu
def main():
    while True:
        print("\n📌 Expense Tracker Menu:")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Edit Expense")
        print("4️⃣ Delete Expense")
        print("5️⃣ Filter by Category")
        print("6️⃣ Monthly Expense Summary")
        print("7️⃣ Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            filter_by_category()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
