liste = []

print("Welcome! Enter your numbers into the list. Type 'calcul' if you want to see the min and max!")

while True:
    number = input('Please add a number to the list: ')

    try:
        float(number)
        liste.append(float(number))

    except ValueError:
        print("Please enter a number")

    if number.lower() == 'calcul':
        break


def moyenne():
    y = 0
    
    for x in liste:
        y = x + y
    
    mean = y / len(liste)
    
    return mean


if liste:
    print('The average is:', moyenne())
else:
    print('Your list is empty!')
