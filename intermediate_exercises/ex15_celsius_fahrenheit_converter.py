def menu():
    while True:
        try:
            value = int(input("Please enter 1 for [Celsius to Fahrenheit] or 2 for [Fahrenheit to Celsius]: "))
        
            if value == 1:
                Celsius_to_Fahrenheit()
                break
        
            elif value == 2:
                Fahrenheit_to_Celsius()
                break
        
        except ValueError:
            print("Error!")


def Celsius_to_Fahrenheit():    
    cel_val = float(input("Please enter the value in Celsius: "))
    farh_val = (cel_val * 9/5) + 32

    print(f'Your value in Celsius: {cel_val} °C is equal to {farh_val} °F')


def Fahrenheit_to_Celsius():
    farh_val = float(input("Please enter the value in Fahrenheit: "))
    cel_val = (farh_val - 32) * 5/9

    print(f'Your value in Fahrenheit: {farh_val} °F is equal to {cel_val} °C')


menu()
