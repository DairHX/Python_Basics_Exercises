from math import sqrt

def welcome_message():
    print("Bienvenue dans le logiciel de résolution des équations du second degré !")
    print('Pour résoudre l\'équation ax² + bx + c = 0, entrez les valeurs de a, b, et c.')

def num_checker():
    while True:
        try:
            a = float(input('Veuillez entrer la valeur de a (non nul) : '))
            if a == 0:
                print("La valeur de a ne doit pas être égale à 0. Recommencez.")
                continue
            b = float(input('Veuillez entrer la valeur de b : '))
            c = float(input('Veuillez entrer la valeur de c : '))
            return a, b, c
        except ValueError:
            print('Veuillez entrer un nombre valide ! \n')

def equation_solver(a, b, c):
    delta = b**2 - 4*a*c  # Calcul du discriminant
    
    print(f"Le discriminant (delta) est : {delta}")

    if delta > 0:
        sol1 = (-b + sqrt(delta)) / (2*a)
        sol2 = (-b - sqrt(delta)) / (2*a)
        return sol1, sol2
    elif delta == 0:
        sol = -b / (2*a)
        return sol, None
    else:
        print("Il n'y a pas de solution réelle.")
        return None, None

def display_solutions(sol1, sol2):
    if sol1 is not None and sol2 is not None:
        print(f"Les solutions de votre équation sont : {sol1:.2f} et {sol2:.2f}")
    elif sol1 is not None:
        print(f"La seule solution de votre équation est : {sol1:.2f}")
    else:
        print("Pas de solution réelle pour cette équation.")

# Exécution du programme
welcome_message()
a, b, c = num_checker()
sol1, sol2 = equation_solver(a, b, c)
display_solutions(sol1, sol2)
