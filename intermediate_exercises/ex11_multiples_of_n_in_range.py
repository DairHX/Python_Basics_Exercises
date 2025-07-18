liste = []

print("This program will return all multiples of a given number n between two bounds a and b (inclusive).")

def get_values():
    n = int(input("Please enter the number n: "))
    a = int(input("Please enter the lower bound a: "))
    b = int(input("Please enter the upper bound b: "))

    return n, a, b


def find_multiples(n, a, b):
    for x in range(a, b + 1):
        if x % n == 0:
            liste.append(x)

    return liste


n, a, b = get_values()
result = find_multiples(n, a, b)

print("Here is the list of multiples of", n, "between", a, "and", b, ":")
print(result)
