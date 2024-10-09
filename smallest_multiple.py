# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder, what is the
# smallest positive number that is evenly divisible by all the numbers from 1 to 20.
# first let's break down what this actually is asking

def smallest_divisible_by_one_to_twenty():
    # keep loop going until conditions met
    divisible_by_all = False
    count = 2520
    while not divisible_by_all:
        # where we start as we know 2520 is smallest divisible by all 10, so will be where we start
        # count = 2520
        all_twenty = 0
        # using range to establish every factor from one to 20
        for i in range(1, 21):
            if count % i == 0:
                all_twenty += 1
        if all_twenty == 20:
            print(f"the final number is {count}")
            divisible_by_all = True
        count += 1
        print(count)


smallest_divisible_by_one_to_twenty()

# this took just over 5 minutes to brute force it, there must be a better way.
