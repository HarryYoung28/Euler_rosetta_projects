# the prime factors of 13195 are 5, 7, 13, and 29.
# what is the largest prime factor of 600851475143?
# BIGo notation this doesn't scale well
# number_total = 233249929
# highest_factor = 0
#
# # first lets work out how to find ANY factor of this number.
# # so factors between 2 and the number total (upto but not including) are checked using modulo
# for factor in range(2, number_total):
#     # if the modulo is 0 then it is a factor so next check
#     if number_total % factor == 0:
#         not_prime = False
#         for x in range(2, factor):
#             # if the factor of the number total is NOT a prime number (it has factors other than 1 and itself)
#             # then continue
#             if factor % x == 0:
#                 not_prime = True
#         if (factor > highest_factor) and (not not_prime):
#             highest_factor = factor
#
# print(highest_factor)
import math


def prime_factor(num):
    # count the number of times that 2 is going to divide
    count = 0

    # while the number can cleanly be divided by 2
    while not (num % 2 > 0):
        num = num / 2
        count += 1

    # if 2 does divide it
    if count > 0:
        print(2, count)

    # now check for all other possible factors by providing a range of 3 and the square root of the number (factors
    # will repeat after the square root), in steps of 2 (only odd numbers can be prime above 2)
    for i in range(3, int(math.sqrt(num)) + 1, 2):

        # repeat count for next factor
        count = 0

        # whilst the number can be divided by factor
        while num % i == 0:
            # add to count
            count += 1
            # divide number by factor and replace number
            num = int(num / i)

        # if there is a count for the factor
        if count > 0:
            print(i, count)


prime_factor(13195)

result = 71 * 839 * 1471 * 6857
print(result)
