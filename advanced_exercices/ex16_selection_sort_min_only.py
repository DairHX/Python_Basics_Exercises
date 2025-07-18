liste = []
new_liste = []

print("Welcome! This program will sort a list using selection sort logic by repeatedly extracting the smallest element.")
print('To stop entering numbers and start sorting, type "calcul".')

def liste_mgmt():
    while True:
        a = input("Please enter a number to add to your list: ")

        if a.lower() == "calcul":
            break

        try:
            a = float(a)
            liste.append(a)

        except ValueError:
            print("Please enter a valid number, not letters!")

    return liste


def newliste_generator():
    print("\nSorting the list using selection sort...")
    
    while True:
        for x in liste:
            if x == min(liste):
                new_liste.append(x)
                liste.remove(x)

        if len(liste) == 0:
            break

    return new_liste


liste_mgmt()
result = newliste_generator()
print("The sorted list is:", result)
