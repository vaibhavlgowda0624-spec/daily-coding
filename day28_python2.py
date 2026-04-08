sentence = input("Enter sentence: ").split()

longest = max(sentence, key=len)

print("Longest word:", longest)
