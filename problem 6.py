#problem 6

num = int(input("Enter a number to show its multiplacation table"))
result = 0

for i in range(11):
    result = num * i
    print (num, "x", i, "=",result)
    
