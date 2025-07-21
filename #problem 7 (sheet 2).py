#problem 7 (sheet 2)

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))



def find_gcd(x, y):
    while y != 0:
        print("x ",x)
        print("y ",y)
        x, y = y, x % y
    return x

gcd = find_gcd(a, b)
lcm = abs(a * b) // gcd
print("The LCM is:", lcm)
