liste = []

print('To calculate the sum of squares, please enter "calcul"!')


def liste_mgmt():
    while True:
        a = input('Please enter a number to add to your list: ')

        if a.lower() == 'calcul':
            break

        try:
            float(a)
            liste.append(a)

        except ValueError:
            print('Please enter a number, not letters!')

    return liste



def sum_liste():
    sum = 0
    for x in liste_mgmt():
        x = float(x)
    
        square_x = x**2

        sum += square_x
    
    return sum


square_sum = sum_liste()

print(square_sum)
