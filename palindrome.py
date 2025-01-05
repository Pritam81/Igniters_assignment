def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())
    return string == string[::-1]

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

if __name__ == "__main__":
    main()