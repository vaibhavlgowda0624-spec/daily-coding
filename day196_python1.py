def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")
