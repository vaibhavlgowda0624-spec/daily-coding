text = input("Enter text: ").lower()

vowels = 0
consonants = 0

for character in text:

    if character.isalpha():

        if character in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
