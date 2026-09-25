expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expense = {
            "item": item,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n--- Your Expenses ---")

            for expense in expenses:
                print(
                    expense["item"],
                    "- ₹", expense["amount"],
                    "-", expense["category"]
                )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Spending: ₹", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")