filename = input("Enter filename: ")

with open(filename, "r") as file:
    print("Total Lines:", len(file.readlines()))
