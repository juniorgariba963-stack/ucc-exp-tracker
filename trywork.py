expenses = []
choice = ""

while choice != 5:
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Show total spending")
    print("4. Update Expense")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 2:
        amount = int(input("How much did you spend? "))
        print("You spent:", amount)
        category = input("Enter the category you spent on (food, transport, entertainment, utilities, healthcare, education, clothing, personal care, insurance, savings, miscellaneous): ")
        print("You spent on:", category)
        spend = input("What did you buy? ")
        print("You bought:", spend)
        expen = {"category": category, "amount": amount, "spend": spend}
        expenses.append(expen)

    elif choice == 1:
        if not expenses:
            print("No expenses recorded.")
        for expense in expenses:
            print("Amount:", expense["amount"], "Category:", expense["category"], "Spend:", expense["spend"])

    elif choice == 3:
        total_spending = 0
        for expense in expenses:
            total_spending += expense["amount"]
        print("Total spending:", total_spending)

    elif choice == 4:
        print("Update expense functionality not implemented yet.")

    elif choice == 5:
        print("Goodbye!")

    else:
        print("Invalid choice. Please select a valid option.")
