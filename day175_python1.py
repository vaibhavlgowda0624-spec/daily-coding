number = int(input("Enter number: "))

if number <= 1:
    print(number)
else:
    dp = [0] * (number + 1)

    dp[1] = 1

    for i in range(2, number + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print("Fibonacci:", dp[number])
