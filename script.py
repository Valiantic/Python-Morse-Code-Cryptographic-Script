# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  
}

def text_to_morse(text):
  
    words = text.upper().split()
    
    morse_words = []
    for word in words:
        morse_chars = []
        for char in word:
            # GET MORSE CODE FOR EVERY CHARACTER
            if char in MORSE_CODE_DICT:
                morse_chars.append(MORSE_CODE_DICT[char])
        # JOIN CHARACTERS BETWEEN SPACE 
        morse_word = ' '.join(morse_chars)
        morse_words.append(morse_word)
    
    # JOIN WORDS BETWEEN SLASH
    return ' / '.join(morse_words)


input_text = input("Enter text to convert to Morse code: ")

# CONVERTION 
morse_result = text_to_morse(input_text)

# DISPLAY THE RESULT
print("Morse code:")
print(morse_result)