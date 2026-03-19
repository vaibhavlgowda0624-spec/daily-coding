num = int(input("Enter number: "))
s = sum(int(i)**3 for i in str(num))

if s == num:
   print("Armstrong")
else:
   print("Not Armstrong")
