#problem 2 (sheet 2)

def sum_digits(number):
    number = str(abs(number))
    total = 0

    for digit in number:
        total += int(digit)
    return total

number = int(input("enter a number"))
print ("sum of numbers is", sum_digits(number))