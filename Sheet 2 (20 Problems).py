#Sheet 2 (20 Problems)

'''
#problem 1

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year"))

if is_leap_year(year):
    print ("year is a leap year")
else:
    print ("year is not a leap year")




#problem 2

def sum_digits(number):
    number = str(abs(number))
    total = 0

    for digit in number:
        total += int(digit)
    return total

number = int(input("enter a number"))
print ("sum of numbers is", sum_digits(number))



#problem 3
 
result = 0


def fibi_seq (n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        result = fibi_seq (n-1) + fibi_seq (n-2)
        return result
    
n = int(input("Enter how many Fibonacci numbers you want: "))

num1, num2 = 0, 1

print(f"The first {n} Fibonacci numbers are:")

for i in range(n):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2



#problem 4

def armstrong_check (number):
    num_str = str(number)
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power
    
    return total == number

number = int(input("enter a number"))

if armstrong_check(number):
    print ("it is an armstrong number")
else:
    print ("it isnt an armstrong number")


#problem 5

def is_perfect_number(n):
    if n <= 0:
        return False

    sum_of_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == n

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")


#problem 6

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


#problem 7

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


#problem 8

def number_to_words(n):
    if not (1 <= n <= 1000):
        return "Number out of range"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"
    words = ""
    if n >= 100:
        words += ones[n // 100] + " hundred"
        if n % 100 != 0:
            words += " and "
        n = n % 100
    if n >= 20:
        words += tens[n // 10]
        if n % 10 != 0:
            words += "-" + ones[n % 10]
    elif n >= 10:
        words += teens[n - 10]
    elif n > 0:
        words += ones[n]
    return words


num = int(input("Enter a number between 1 and 1000: "))
print(number_to_words(num))


#problem 9

binary_string = input("Enter a binary number: ")

for char in binary_string:
    if char not in '01':
        print("Invalid binary number")
        break
else:
    decimal_value = 0
    for bit in binary_string:
        decimal_value = decimal_value * 2 + int(bit)
    print(decimal_value)


#problem 10

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    
    return binary

num = int(input("Enter a decimal number: "))
print(f"The binary representation of {num} is {decimal_to_binary(num)}")


#problem 11

import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        return " Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"

# Example
password = input("Enter your password: ")
print("Strength:", check_password_strength(password))



#problem 12

def int_to_roman_1000(number):
    if not 0 < number <= 1000:
        return "Number out of range (must be between 1 and 1000)"
    
    value = [1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4, 1]
    
    symbols = ["M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"]
    
    roman_digit = ""
    i = 0

    while number > 0:
        for _ in range(number // value[i]):
            roman_digit += symbols[i]
            number -= value[i]
        i += 1

    return roman_digit

num = int(input("Enter a number between 1 and 1000: "))
print("Roman numeral:", int_to_roman_1000(num))



#problem 13

def print_diamond(n):
 
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

  
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)


N = int(input("Enter N: "))
print_diamond(N)


#problem 14

def collatz_sequence(n):
    while n != 1:
        print(n, end="--->")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

num = int(input("Enter a number: "))
collatz_sequence(num)


#problem 15

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'  # Using '/' to separate words
}

def to_morse_code(text):
    morse = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + " "
        else:
            morse += "? "  # unknown character
    return morse.strip()

# Example usage
text = input("Enter text to convert to Morse code: ")
print("Morse Code:", to_morse_code(text))



#problem 16

def time_difference(time1, time2):
    hour1, minute1 = map(int, time1.split(":"))
    hour2, minute2 = map(int, time2.split(":"))

    total1 = hour1 * 60 + minute1
    total2 = hour2 * 60 + minute2

    return abs(total1 - total2)

time1 = input("Enter first time (HH:MM): ")
time2 = input("Enter second time (HH:MM): ")
print("Difference in minutes:", time_difference(time1, time2))


#problem 17

import tkinter as tk
from tkinter import messagebox

# Functions for each menu action
def add_numbers():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        result_label.config(text=f"Sum = {a + b}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

def subtract_numbers():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        result_label.config(text=f"Difference = {a - b}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

def exit_app():
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("Simple Python Menu GUI")
root.geometry("300x250")

# Labels and input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Menu buttons
tk.Button(root, text="Add", command=add_numbers).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_numbers).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()

'''