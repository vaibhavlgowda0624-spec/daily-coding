import csv

total = 0
count = 0

with open("marks.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["marks"])
        count += 1

print("Average:", total / count)
