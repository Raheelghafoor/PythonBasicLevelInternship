#problem 2

n_Limit = int(input("enter the limit upto which you wish for the sum to be calculated"))
sum = 0

for i in range(n_Limit):
    sum = sum + i
    
print ("the sum is", sum)