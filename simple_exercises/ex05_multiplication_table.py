a = float(input('Please enter a number: '))

b = int(input("Enter the number up to which the multiplication table should go: "))

for x in range(1, b + 1):
    print('Here is the multiplication table of your number:', a * x)
