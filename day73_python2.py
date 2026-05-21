word = input("Word: ")

with open("test.txt") as f:
    print(word in f.read())
