balance = 5000

print("1.Withdraw")
print("2.Check Balance")

choice = int(input())

if choice == 1:
    amt = int(input("Amount: "))
    balance -= amt
    print(balance)
else:
    print(balance)
