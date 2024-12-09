# 1. Having 2 variables: A = 5 and B= 7, how do you do to interchange values
# so A = 7 and B = 5?

# Initial values
A, B = 5, 7


# Swapping values
A, B = B, A


# Result
print("A =", A, "B =", B)


# 2. Having 2 lists: List A with 10 different numbers and List B with 4 different
# numbers, how do you do to print 4 lines where in line 1 we need to have
# all the numbers from list A multiplied by the 1st number of list B,
# in the line 2 all the numbers of the list A multiplied by the 2nd number of list B
# and go on for the 4 lines?

# Initial lists
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_B = [2, 3, 5, 7]

# Generate the 4 lines
for i in range(len(list_B)):  # Iterate over indices of list_B
    result_line = [a * list_B[i] for a in list_A]  # Multiply each item in list_A by list_B[i]
    print(f"Line {i+1}: {result_line}")


# 3. Having a call/request to an outer component you don't have control over it.
# The component returns many errors, so we need to assure we repeat the call
# until it returns the right value or maximum 5 times if always returns error.
# If the call returns a value, we print it and if it returns error for all the tries we do,
# we print error.

# Simulating an outer component call
import random


def external_call():
    # Randomly simulates success or error
    return "value" if random.choice([True, False]) else "error"


# Retry logic
max_retries = 5
for attempt in range(1, max_retries + 1):
    response = external_call()
    if response != "error":
        print(response)
        break
    elif attempt == max_retries:
        print("error")