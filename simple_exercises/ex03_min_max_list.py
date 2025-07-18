print('Welcome to the min and max calculator!')
print('''If you want to stop entering elements into the list, type "calcul"!''')

liste = []

while True:
    number = input("Please enter an element for the list: ")
   
    if number == "calcul":
        break
    
    try:
        number = float(number)
        liste.append(number)

    except ValueError:
        print('Error')

    print(liste)

print('Here is the final list you created:', liste)
print('Here is the minimum of the list:', min(liste))
print('Here is the maximum of the list:', max(liste))
