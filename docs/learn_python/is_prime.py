def is_prime(number):
    # numbers less that or equal to 1 are not prime
    if number <= 1:
        return False
    # Since 0 and 1 are not prime, we start from 2
    for i in range(2, number):
        # If the number is divisible by any number other than 1 and itself, it is NOT prime
        # Numbers here are only whole-numbers (0-9)
        if number % i == 0:
            return False
    # If the number is not divisible by any number other than 1 and itself, it IS prime
    return True
