import json
from datetime import datetime

# Expense entry class
class Expense:
    def __init__(self, date, amount, category, notes=None):
        self.date = date
        self.amount = amount
        self.category = category
        self.notes = notes

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "notes": self.notes if self.notes else ""
        }

# Function to add an expense
def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    notes = input("Enter any notes (optional): ")
    if not notes:
        notes = None
    expense = Expense(date, amount, category, notes)
    expenses.append(expense.to_dict())

# Function to save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=4)

# Load expenses from file (if exists)
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    expenses = load_expenses()
    while True:
        add_expense(expenses)
        save_expenses(expenses)
        another = input("Do you want to add another expense? (y/n): ")
        if another.lower() != 'y':
            break
