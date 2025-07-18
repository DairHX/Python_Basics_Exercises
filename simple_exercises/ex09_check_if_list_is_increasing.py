liste = []

print('To check if your list is increasing, type "calcul"!')

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


def verify_liste():
    for x in range(0, len(liste) - 1):
        compare = liste[x + 1] - liste[x]

        if compare < 0:
            print("Your list is not in increasing order.")
            break

    else:
        print("Your list is in increasing order!")


liste_mgmt()
verify_liste()
