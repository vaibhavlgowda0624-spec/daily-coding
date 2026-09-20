def calculate_sum(n):
    if n == 0:
        return 0

    return n + calculate_sum(n - 1)


number = int(input("Enter a number: "))

print("Sum:", calculate_sum(number))
