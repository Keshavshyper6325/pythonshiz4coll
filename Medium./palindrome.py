def palindromeCheck(s):
    return s == s[::-1]

st = str(input("Enter a String: "))

match palindromeCheck(st):
    case 0:
        print("Not a palindrome.")
    case 1:
        print("Palindrome!")
    case _:
        print("Invalid String")