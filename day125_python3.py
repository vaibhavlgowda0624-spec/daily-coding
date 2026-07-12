balance = 5000

print("1.Check Balance")
print("2.Deposit")

choice = int(input())

if choice == 1:
    print(balance)
elif choice == 2:
    amount = int(input())
    balance += amount
    print(balance)
