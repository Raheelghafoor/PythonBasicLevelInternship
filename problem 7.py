#problem 7

text = input("Enter a string: ")
reversed_Text = ""

for char in text:
    reversed_Text = char + reversed_Text

print("Reversed string:", reversed_Text)

if reversed_Text == text:
    print ("your string is a palindrome")
else:
    print ("it is not a palindrome")
