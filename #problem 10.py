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
