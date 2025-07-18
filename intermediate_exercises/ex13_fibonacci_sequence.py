Un = [0, 1]

def Fibonacci():
    while True:
        try: 
            n = int(input("Please enter a number >= 2: "))
            
            if n >= 2:
                break
            else:
                print('Enter a number greater than or equal to 2!')

        except ValueError:
            print('Error! Please enter a positive integer!')

    for x in range(2, n):
        fib_val = Un[x - 1] + Un[x - 2]
        Un.append(fib_val)
        
    return Un

result = Fibonacci()

print(result)
