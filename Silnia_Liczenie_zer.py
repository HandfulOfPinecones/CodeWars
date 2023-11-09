import math


# You can count the number of trailing zeros in a Python integer by converting
# the integer to a string and then counting the zeros from the right.
def zeros(n):
    # Factorial solution
    silnia = str(math.factorial(n))

    # Initialize a count to keep track of trailing zeros
    count = 0

    # Iterate through the characters in the string from right to left
    for char in reversed(silnia):
        if char == "0":
            count += 1
        else:
            break  # Exit the loop as soon as a non-zero character is encountered

    return count


# Examples:
print(zeros(0))  # Output: 0
print(zeros(6))  # Output: 1
print(zeros(30))  # Output: 7
print(zeros(100000))  # Output: 24999


# If you need to handle very large numbers that exceed the limit for integer string conversion
# (e.g., greater than the maximum value that can be represented by an int in Python),
# you can still count the trailing zeros using mathematical operations without converting the number to a string.
# Here's a modified approach for large numbers:
def zeros_over_limit(n):
    silnia = math.factorial(n)
    count = 0
    # This function works by repeatedly dividing the number by 10 and counting the divisions until the number is no longer divisible by 10.
    # Unfortunately it's slow as fuck
    while silnia % 10 == 0 and silnia != 0:
        count += 1
        silnia //= 10

    return count


print(zeros_over_limit(0))  # Output: 0
print(zeros_over_limit(6))  # Output: 1
print(zeros_over_limit(30))  # Output: 7
print(zeros_over_limit(100000))  # Output: 24999


# For last solution you dont have to even solve the factorial
# For last solution you dont have to even solve the factorial
# https://mathworld.wolfram.com/Factorial.html
def zeros_not_calc(n):
    if n < 2:
        return 0
    else:
        k_max = math.floor(math.log(n, 5))
        Z = 0.0  # Initialize Z to zero

        for k in range(1, k_max + 1):
            Z += math.floor(n / (5**k))

        return math.floor(Z)  # Z needs to be rounded down


print(zeros_not_calc(0))  # Output: 0
print(zeros_not_calc(6))  # Output: 1
print(zeros_not_calc(30))  # Output: 7
print(zeros_not_calc(100000))  # Output: 24999
