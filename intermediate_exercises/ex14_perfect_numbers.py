print("Enter the upper limit up to which you want to check for perfect numbers!")

while True:   
    try:
        n = int(input("Please enter a positive integer: "))
        
        if n > 0:
            break

    except ValueError:
        print("Error!")

nb_entier = range(0, n)


def verification_nb_entier(number):
    perfect = 0
    
    for x in range(1, number):
        diviseur = number % x

        if diviseur == 0:
            perfect = perfect + x
        
    if perfect == number:
        print(f"{number} is a perfect number!")


for number in nb_entier:
    verification_nb_entier(number)
