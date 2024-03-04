"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"""
1.A ValueError will occur when the user enters a non-integer value for the numerator or denominator.

2.A ZeroDivisionError will occur when the user enters 0 for the denominator.

3.Yes, to avoid the possibility of a ZeroDivisionError, we can add a condition to check if the denominator is 0 before dividing.
"""

