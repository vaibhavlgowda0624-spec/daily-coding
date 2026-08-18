expenses = {
    "Food": 1200,
    "Travel": 800,
    "Books": 1500,
    "Entertainment": 700
}

total = sum(expenses.values())

highest = max(
    expenses,
    key=expenses.get
)

print("Total Expense:", total)
print("Highest Category:", highest)
