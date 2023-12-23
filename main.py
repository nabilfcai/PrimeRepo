def is_prime(number:int) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check for factors up to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Example usage:
number_to_check = 17
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

def is_even(number: int) -> bool:
    return number % 2 == 0

 # Example usage:
number_to_check = 8
if is_even(number_to_check):
    print(f"{number_to_check} is a even number.")
else:
    print(f"{number_to_check} is odd number.")