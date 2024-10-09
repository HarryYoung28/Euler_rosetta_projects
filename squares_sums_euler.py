# the sum of the squares of the first 10 natural numbers is  1sq + 2sq e.t.c = 385
# the square of the sum of the first ten natural numbers is (1 + 2 + 3 e.t.c)sq = 55sq = 3025
# hence the diff between the sum of the squares and the square of the sum is 3025 - 385 = 2640
# find the difference between the sum of the squares and of the first one hundred natural numbers and the square of the
# sum

result = 0
# in range 1-100 square each number and add together
for i in range(1, 101):
    square = i ** 2
    result += square

print(f"The sum of the squares is {result}")

total_sum = 0
# in range 1-100 add the numbers
for i in range(1, 101):
    total_sum += i

print(f"The total sum of the numbers before they are squared is {total_sum}")
# square the numbers that were added
sum_squared = total_sum ** 2

print(f"The square of the sums is {sum_squared}")

# find the difference by removing the square of the sums (the higher number logically) with the sum of the squares
final_result = sum_squared - result
print(f"The final result is {final_result}")


