import random

num = random.randint(1, 10)

for i in range(3):
    guess = int(input("Guess: "))
    if guess == num:
        print("Correct")
        break
else:
    print("Out of attempts. Number:", num)
  
