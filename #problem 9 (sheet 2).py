#problem 9 (sheet 2)

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
