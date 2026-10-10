expense =[]
while True:
    print("\n----Expense Tracker----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3.show total")
    print("4. Exit")
    choice = input("Enter your choice : ")
    if choice =="1":
        item = input("Enter expense item: ")
        amount = float(input("Enter expense amount: "))
        expense.append({"item":item,"amount": amount})
        print("Expense added successfully!")
    elif choice =="2":
        if len(expense) == 0:
            print("No expenses recorded.")
        else:
            for item in expense:
                print(item["item"], "-rs", item["amount"])
    elif choice =="3":
        total=0
        for item in expense:
            total += item["amount"]
        print("Total expenses: rs.", total)
    elif choice =="4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")

