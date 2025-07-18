liste = []
prime_liste = []

print('Enter as many whole numbers as you want!')

def liste_mgmt():
    while True:
        a = input('Please enter a number to add to your list: ')

        if a.lower() == 'calcul':
            break

        try:
            a = float(a)
            liste.append(a)

        except ValueError:
            print('Please enter a valid number, not letters!')

    return liste


def nb_premier():
    for nombre in liste:
        i = 0

        for x in range(1, int(nombre) + 1):
            test_number = nombre % x

            if test_number == 0:
                i = i + 1

        if i == 2:
            prime_liste.append(nombre)
        else:
            continue

    return prime_liste

liste_mgmt()

val_new_liste = nb_premier()

print("Here are the prime numbers you entered:", val_new_liste)
