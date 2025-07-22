#Sheet 4 (Logical Mastery)

#Problem 1

'''num = int(input("Enter a number: "))

while num >= 10:
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    num = sum_digits

print("Final single digit:", num)'''

#Problem 2

num = int(input("Enter a number: "))
square = num * num
digits = 0
temp = num


while temp > 0:
    digits += 1
    temp //= 10

divisor = 10 ** digits

right = square % divisor
left = square // divisor


if left + right == num:
    print(f"{num} is a Kaprekar number")
else:
    print(f"{num} is NOT a Kaprekar number")


#problem 3

text = input("Enter a string: ")
text = text.lower()

for char in text:
    if char.isalpha():
        position = ord(char) - ord('a') + 1
        print(position, end=" ")

#problem 4

num = int(input("Enter a number: "))

while num >= 10:
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    num = sum_digits

if num == 1:
    print("It is a Magic Number")
else:
    print("It is NOT a Magic Number")

#problem 5

n = int(input("Enter a number: "))
count = 0
i = 5

while n // i > 0:
    count += n // i
    i *= 5

print("Trailing zeros in", n, "factorial:", count)

#problem 6

for num in range(1, 501):
    
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            
            if str(num) == str(num)[::-1]:
                print(num)

#problem 7

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})")


#problem 8

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    sum_digits += temp % 10
    temp = temp // 10


if num % sum_digits == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is NOT a Harshad number")

#problem 9

for num in range(1, 101):
    if num % 4 == 0 and num % 6 == 0:
        print("CracklePop")
    elif num % 4 == 0:
        print("Crackle")
    elif num % 6 == 0:
        print("Pop")
    else:
        print(num)

#problem 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_harshad(n):
    sum_digits = 0
    temp = n
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    return n % sum_digits == 0

print("Super Numbers (Prime + Palindrome + Harshad) under 1000:")
for num in range(1, 1000):
    if is_prime(num) and is_palindrome(num) and is_harshad(num):
        print(num)




