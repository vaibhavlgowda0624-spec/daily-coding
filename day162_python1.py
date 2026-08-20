memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]

number = int(input("Enter number: "))

print(fibonacci(number))
