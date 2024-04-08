def find_factors(n):
    """
    Returns a list containing all the factors of a given number.
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

num = int(input('enter the number '))
result = find_factors(num)
print(result)


while True:
    try:
        # Get the number from the user
        num = int(input("Enter a positive integer (or enter '0' to exit): "))
        if num == 0:
            print("Exiting the program. Have a great day!")
            break
        result = find_factors(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a positive integer or '0' to exit.")
