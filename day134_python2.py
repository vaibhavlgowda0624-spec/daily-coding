import csv

rows = [
    ["Name","Marks"],
    ["Vaibhav",92],
    ["Rahul",81]
]

with open("result.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerows(rows)

print("CSV Created")
