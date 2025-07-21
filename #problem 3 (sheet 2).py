#problem 3 (sheet 2)

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
