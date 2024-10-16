# by listing the first few prime numbers, 2, 3, 5, 7, 11, 13, we can see that the 6th prime number is 13,
# what is the 10001st prime number?
import math


def find_the_10001st_prime():
    # we already know that 6th prime number is 13, again so count is 6 and number starts at 14
    count = 6
    number = 14
    # get to count to 10001 primes
    while count < 10001:
        # checks for prime
        is_prime = True
        # for i in range between 2 and the square root the int(math.sqrt) will return the floor of the number if its
        # a decimal
        for i in range(2, int(math.sqrt(number)) + 1):
            # if number cleanly divides by any of the range then it is not a prime
            if number % i == 0:
                # changes is prime to false
                is_prime = False
                # breaks out of the loop once established that not a prime
                break
        # if the number IS prime
        if is_prime:
            # add one to prime number count
            count += 1
            # at 10001st number, print the number
            if count == 10001:
                print(number)
        # add one to number to try next number
        number += 1


find_the_10001st_prime()
