class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, "Not Found")

ht = HashTable()

ht.insert("name", "Vaibhav")
ht.insert("course", "MCA")

print(ht.get("name"))
print(ht.get("course"))
