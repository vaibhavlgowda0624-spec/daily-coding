from collections import Counter

word1 = input("First word: ")
word2 = input("Second word: ")

if Counter(word1.lower()) == Counter(word2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")
