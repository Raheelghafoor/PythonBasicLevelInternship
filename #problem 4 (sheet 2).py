#problem 4 (sheet 2)

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
