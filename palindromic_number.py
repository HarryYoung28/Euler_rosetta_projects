# palindromic numbers read the same back to front
# 9009 = 91 * 99 (largest two-digit numbers that make a palindrome)
# what's largest 3 digit?

previous_result = 0

for i in range(99, 1000):
    for j in range(99, 1000):
        result = i * j
        if str(result) == str(result)[::-1]:
            if result > previous_result:
                previous_result = result

print(f"the largest result is {previous_result}")
