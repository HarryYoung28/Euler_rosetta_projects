# just going to use this to work out a few steps seen online for large prime numbers
import math

first_number = 987653
second_number = 701999
third_number = 538874
fourth_number = 846893
fifth_number = 742621
sixth_number = 629134


def sum_of_digits(x):
    result = 0
    for digit in str(x):
        result += int(digit)

    print(f"the result of the sum of the digits is {result}")
    if result % 3 == 0:
        print("the result is divisible by 3")
    else:
        print("the result is not divisible by 3")


sum_of_digits(first_number)

sum_of_digits(second_number)


def prime_number_check(y):
    is_prime = True

    for i in range(2, int(math.sqrt(y)) + 1):
        if y % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The number {y} is prime.")
    else:
        print(f"The number {y} is NOT prime.")


prime_number_check(first_number)
prime_number_check(second_number)

