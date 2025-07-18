pal_test = ""

palindrome = input("Please enter a string: ")

for x in range(0, len(palindrome)):
    pal_test = pal_test + palindrome[len(palindrome) - 1 - x]

if palindrome == pal_test:
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome!")
