#problem 8 (sheet 2)

def number_to_words(n):
    if not (1 <= n <= 1000):
        return "Number out of range"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"
    words = ""
    if n >= 100:
        words += ones[n // 100] + " hundred"
        if n % 100 != 0:
            words += " and "
        n = n % 100
    if n >= 20:
        words += tens[n // 10]
        if n % 10 != 0:
            words += "-" + ones[n % 10]
    elif n >= 10:
        words += teens[n - 10]
    elif n > 0:
        words += ones[n]
    return words


num = int(input("Enter a number between 1 and 1000: "))
print(number_to_words(num))