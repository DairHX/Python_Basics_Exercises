print("Welcome to the GCD calculator!")

def pgcd_calculator(a, b):
    n = 0
    reste = []
    reste.extend([a, b])  # Instead of reste.append(a) and reste.append(b)
    
    while reste[n] != 0:
        r = reste[n] % reste[n + 1]
        n = n + 1

        if r == 0:
            break
        reste.append(r)

    print(f"Your GCD is: {reste[n]}")
    return r


while True:
    try:
        a = int(input("Please enter a positive integer a: "))
        b = int(input("Please enter a positive integer b: "))

        if a < b:
            print("a must be greater than b!")
            continue  # Ask again for a and b

        if a > 0 and b > 0 and a > b:
            pgcd_calculator(a, b)
            break

    except ValueError:
        print("Error!")
