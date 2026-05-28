votes = {"A":0, "B":0}

choice = input("Vote A/B: ")

if choice in votes:
    votes[choice] += 1

print(votes)
