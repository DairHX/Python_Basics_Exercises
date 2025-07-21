def get_user_input():
    numbers = []
    print('To calculate the average of even numbers, type "calcul"!')

    while True:
        a = input('Please enter a number to add to your list: ')
        if a.lower() == 'calcul':
            break

        try:
            num = int(a)
            numbers.append(num)
        except ValueError:
            print('Please enter a valid integer.')

    return numbers


def average_of_even_numbers(numbers):
    evens = [x for x in numbers if x % 2 == 0]

    if evens:
        average = sum(evens) / len(evens)
        print(f"The even numbers: {evens}")
        print(f"The average of even numbers is: {average}")
    else:
        print("No even numbers found in the list.")


# Run the program
user_numbers = get_user_input()
average_of_even_numbers(user_numbers)
