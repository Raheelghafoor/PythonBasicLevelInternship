#problem 18

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'  # Using '/' to separate words
}

def to_morse_code(text):
    morse = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + " "
        else:
            morse += "? "  # unknown character
    return morse.strip()

# Example usage
text = input("Enter text to convert to Morse code: ")
print("Morse Code:", to_morse_code(text))
