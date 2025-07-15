#problem 9

num = int(input("enter a number: "))

if num < 0:
    print("cannot be calculated")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    print("The factorial of", num , "is" , factorial)
