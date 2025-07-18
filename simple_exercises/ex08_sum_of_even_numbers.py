liste = []

print('To calculate the sum of even numbers, type "calcul"!')

def liste_mgmt():
    while True:
        a = input('Please enter a number to add to your list: ')

        if a.lower() == 'calcul':
            break

        try:
            a = float(a)
            liste.append(a)

        except ValueError:
            print('Please enter a number, not letters!')

    return liste


def sum_liste():
    sum = 0
    for x in liste_mgmt():
        if x.is_integer() and x % 2 == 0:
            print(x)
            sum = x + sum
        else:
            continue

    return sum


pair_sum = sum_liste()

print(f'The sum of even numbers in your list is: {pair_sum}')
