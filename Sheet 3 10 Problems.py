#Sheet 3 (Logical Thinking)

#problem 1

num= int(input("Enter a number: "))
odd_Count = 0

for digit in str(num):
    if int(digit) % 2 != 0:
        odd_Count += 1

print (f"The number of odd digits in {num} is: {odd_Count}")

#problem 2

num = int(input("Enter a number: "))
prod_Digits = 1

for digit in str(num):
    if int(digit) != 0:
        prod_Digits *= int(digit)

print(f"The product of the non-zero digits in {num} is: {prod_Digits}")

#problem 3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print(f"The second largest is: {num1}")
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print(f"The second largest is: {num2}")
elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print(f"The second largest is: {num3}")

#problem 4

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

user_String = input("Enter a string: ")
alphabets_Count = 0
digits_Count = 0
special_Chars_Count = 0
for char in user_String:
    if char in alphabets:
        alphabets_Count += 1
    elif char in digits:
        digits_Count += 1
    elif char in special_chars:
        special_Chars_Count += 1
print (f"the number of alphabets in the string is: {alphabets_Count}")
print (f"the number of digits in the string is: {digits_Count}")
print (f"the number of special characters in the string is: {special_Chars_Count}")

#problem 5

num = int(input("Enter a number: "))

first_Digit = int(str(num)[0])
last_Digit = int(str(num)[-1])

Sum = first_Digit + last_Digit

print (f"the sum of the first and last digit on your number {num} is: {Sum}")

#problem 6

num = int(input("Enter a number: "))

for i in range (1, num):
    if num % i == 0:
        print (f"{i} is factor of {num}")


#problem 7

import math

num = int(input("Enter a number: "))
original = num
sum_Check = 0


for char in str(num):
    sum_Check += math.factorial(int(char))


if sum_Check == original:
        print (f"{original} is a strong number")
else:
        print (f"{original} is not a strong number")

#problem 8

num = int(input("Enter a number: "))
sum_Even = 0

for digit in str(num):
    if int(digit) %2 == 0:
        sum_Even += int(digit)
print(f"The sum of the even digits in {num} is: {sum_Even}")


#problem 9

num = int(input("Enter a number: "))
num_Query = int(input("enter a number to check how many times it appears in the number: "))
count = 0

for digit in str(num):
    if int(digit) == num_Query:
        count += 1
print(f"The digit {num_Query} appears {count} times")

#problem 10

num =int(input("enter a number you want to reverse:"))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10
print(f"The reverse of the number is: {reverse}")

