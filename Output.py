import json
import matplotlib.pyplot as plt
import pandas as pd

# Function to load expenses from file
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Function to generate the pie chart
def generate_pie_chart(expenses):
    # Convert expenses into a DataFrame for easier processing
    df = pd.DataFrame(expenses)
    category_totals = df.groupby('category')['amount'].sum()

    # Plotting the pie chart
    plt.figure(figsize=(7, 7))
    category_totals.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Expense Breakdown by Category')
    plt.ylabel('')  # Remove the label for clarity
    plt.show()

if __name__ == "__main__":
    expenses = load_expenses()
    if expenses:
        generate_pie_chart(expenses)
    else:
        print("No expenses to display.")
