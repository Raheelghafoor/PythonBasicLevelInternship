#Python Sheet 1 (10 Problems)

'''
problem 1

num1 = int(input("enter a number"))

if num1 % 2 == 0 :
    print ("number is even")
else :
    print ("number is odd")



problem 2

n_Limit = int(input("enter the limit upto which you wish for the sum to be calculated"))
sum = 0

for i in range(n_Limit):
    sum = sum + i
    
print ("the sum is", sum)

problem 3
numbers_list = []

for count in range(10):
    user_input = int(input("Enter integer "))
    numbers_list.append(user_input)

max_Value = numbers_list [0]

for number in numbers_list [1:] :
    if number > max_Value:
        max_Value = number

print ("the largest value in the list is", max_Value)

problem 4

text = str(input("enter a string"))

vowel_Key = "aeiouAEIOU"
vowel_Count = 0

for char in text:
    if char in vowel_Key:
        vowel_Count += 1
    
print ("number of vowels in your string are", vowel_Count)

problem 5

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

problem 6

num = int(input("Enter a number to show its multiplacation table"))
result = 0

for i in range(11):
    result = num * i
    print (num, "x", i, "=",result)

problem 7

text = input("Enter a string: ")
reversed_Text = ""

for char in text:
    reversed_Text = char + reversed_Text

print("Reversed string:", reversed_Text)

if reversed_Text == text:
    print ("your string is a palindrome")
else:
    print ("it is not a palindrome")

problem 8

text = input("Enter a string: ")
reversed_Text = ""

for char in text:
    reversed_Text = char + reversed_Text

if reversed_Text == text:
    print ("your string is a palindrome")
else:
    print ("it is not a palindrome")

problem 9

num = int(input("enter a number: "))

if num < 0:
    print("cannot be calculated")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    print("The factorial of", num , "is" , factorial)

problem 10

marks1 = int(input("enter your marks"))
marks2 = int(input("enter your marks"))
marks3 = int(input("enter your marks"))
marks4 = int(input("enter your marks"))
marks5 = int(input("enter your marks"))
sum = int(input("enter your marks"))
sum = 0

sum = marks1 + marks2 + marks3 + marks4 + marks5
avg = sum / 5

if avg >= 50:
    print("pass")
else:
    print ("fail")

'''