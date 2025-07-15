#problem 4

text = str(input("enter a string"))

vowel_Key = "aeiouAEIOU"
vowel_Count = 0

for char in text:
    if char in vowel_Key:
        vowel_Count += 1
    
print ("number of vowels in your string are", vowel_Count)