import os
import json

# Load the JSON file
def load_data():
    if os.path.exists("Budget.json"):
        with open("Budget.json", "r") as file:
            return json.load(file)
    else:
        return {"Expense": []}

# Save data to the JSON file
def save_data(data):
    with open("Budget.json", "w") as file:
        json.dump(data, file)

# Expense and Income Entry
def expense(data, income):
    category = input("Enter the expense category: ")
    amount = float(input("Enter the total paid amount: "))
    data["Expense"].append({"category": category, "amount": amount, "Remaining amount": income})
    save_data(data)
    print("Successfully added expense.")

# Budget Calculation
def budget_calculation(data, income):
    for expense in data["Expense"]:
        remaining_amount = expense["Remaining amount"] - expense["amount"]
        expense["Remaining amount"] = remaining_amount
    save_data(data)
    print("Budget calculations done.")

# Expense analysis
def expense_analysis(data):
    print("########## Expense Analysis ###########")
    print("Category\tAmount\tRemaining Amount")
    for expense in data["Expense"]:
        print(f"{expense['category']}\t\t{expense['amount']}\t{expense['Remaining amount']}")

def main():
    data = load_data()
    income = float(input("Enter the income: "))
    
    while True:
        print("\n1. Add Expense")
        print("2. Budget Calculation")
        print("3. Expense analysis")
        print("4. Exit")
        
        choice = input("Enter your choice: \n")
        if choice == "1":
            expense(data, income)
        elif choice == "2":
            budget_calculation(data, income)
        elif choice == "3":
            expense_analysis(data)
        else:
            break

if __name__ == "__main__":
    main()
