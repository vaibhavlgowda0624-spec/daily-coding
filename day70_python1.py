contacts = {}

while True:
    name = input("Name: ")
    
    if name == "exit":
        break
    
    phone = input("Phone: ")
    contacts[name] = phone

print(contacts)
