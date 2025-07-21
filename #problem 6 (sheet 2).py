#problem 6 (sheet 2)

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))



def find_gcd(x, y):
    while y != 0:
        print("x ",x)
        print("y ",y)
        x, y = y, x % y
    return x

print("The GCD is:", find_gcd(a, b))