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
