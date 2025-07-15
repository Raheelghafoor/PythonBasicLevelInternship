#problem 5

num = int(input("enter a number:"))

if num <= 1:
    print ("number is not prime")
    
else:
    prime_Check = True
    
for i in range(2, num):
    if num % i == 0:
        prime_Check = False
        break
    
if prime_Check == True:
    print ("number is prime")
else:
    print ("number is not prime")
    