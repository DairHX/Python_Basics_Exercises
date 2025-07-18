print("Please enter the values of a and b to solve your equation ax + b = 0\n")

while True:
    a = float(input("Please enter the value of a: "))
    if a != 0:
        break
    else:
        print('Please enter a number different from 0:\n')
        continue

b = float(input("Please enter the value of b: "))

print(f'The solution of your equation is: x = {-b / a}')
