#problem 3
numbers_list = []

for count in range(10):
    user_input = int(input("Enter integer "))
    numbers_list.append(user_input)

max_Value = numbers_list [0]

for number in numbers_list [1:] :
    if number > max_Value:
        max_Value = number

print ("the largest value in the list is", max_Value)
