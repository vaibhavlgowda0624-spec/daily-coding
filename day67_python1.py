balance = 1000

withdraw = int(input("Withdraw amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Remaining:", balance)
else:
    print("Insufficient Balance")
