import csv

with open("a.csv") as a, open("b.csv") as b:
    reader1 = csv.reader(a)
    reader2 = csv.reader(b)

    rows = list(reader1) + list(reader2)

with open("merged.csv","w",newline="") as out:
    writer = csv.writer(out)

    writer.writerows(rows)

print("Merged Successfully")
