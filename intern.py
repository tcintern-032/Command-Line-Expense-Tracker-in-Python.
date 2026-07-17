import json
import os
FILE_NAME = "expenses.json"
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return[]
# Save Expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)
# Add Expenses
def add_expense(expenses):
    try:
        name = input("Enter expense name: ")

        amount = float(input("Enter amount: "))

        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        save_expenses(expenses)

        print("\nExpense Added Successfully!\n")

    except ValueError:
        print("\nInvalid amount!\n")
# View Expenses
def view_expenses(expenses):

    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n------ Expense List ------")

    for index, expense in enumerate(expenses, start=1):

        print(f"{index}. {expense['name']}")

        print(f"   Amount   : ${expense['amount']}")

        print(f"   Category : {expense['category']}")

        print("--------------------------")
# Delete Expense
def delete_expense(expenses):

    view_expenses(expenses)

    if not expenses:
        return

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):

            deleted = expenses.pop(choice - 1)

            save_expenses(expenses)

            print(f"\nDeleted: {deleted['name']}\n")

        else:
            print("\nInvalid number!\n")

    except ValueError:
        print("\nEnter a valid number!\n")
# Total Expense
def total_expenses(expenses):

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses = ${total:.2f}\n")
# Search Category

def search_category(expenses):

    category = input("Enter category: ").lower()

    found = False

    print()

    for expense in expenses:

        if expense["category"].lower() == category:

            print(expense)

            found = True

    if not found:
        print("No expense found in this category.")

    print()
# Summary by Category
def summary_category(expenses):

    summary = {}

    for expense in expenses:

        category = expense["category"]

        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n------ Category Summary ------")

    for category, total in summary.items():

        print(f"{category}: ${total:.2f}")

    print()
# Main Menu
def main():

    expenses = load_expenses()

    while True:

        print("========= Expense Tracker =========")

        print("1. Add Expense")

        print("2. View Expenses")

        print("3. Delete Expense")

        print("4. Calculate Total Expense")

        print("5. Search by Category")

        print("6. Summary by Category")

        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            delete_expense(expenses)

        elif choice == "4":

            total_expenses(expenses)

        elif choice == "5":

            search_category(expenses)

        elif choice == "6":

            summary_category(expenses)

        elif choice == "7":

            print("\nThank you for using Expense Tracker!")

            break

        else:

            print("\nInvalid choice! Please try again.\n")


if __name__ == "__main__":
    main()