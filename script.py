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

# REVERSE MODE FOR DECODING 
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

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

def morse_to_text(morse_code):
    # Split Morse code into words
    morse_words = morse_code.strip().split(' / ')
    
    text_words = []
    for morse_word in morse_words:
        # Split Morse word into characters
        morse_chars = morse_word.split(' ')
        text_chars = []
        for char in morse_chars:
            # Get text for each Morse character, ignore if not found
            if char in REVERSE_MORSE_CODE_DICT:
                text_chars.append(REVERSE_MORSE_CODE_DICT[char])
        # Join characters to form the word
        text_word = ''.join(text_chars)
        text_words.append(text_word)
    
    # Join words with spaces
    return ' '.join(text_words)

def main():
    print("Morse Code Converter")
    print("1. Convert Text to Morse Code")
    print("2. Convert Morse Code to Text")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
     
        input_text = input("Enter text to convert to Morse code: ")
        morse_result = text_to_morse(input_text)
        print("Morse code:")
        print(morse_result)
    elif choice == '2':
        
        input_morse = input("Enter Morse code to convert to text (use ' / ' for word separation): ")
        text_result = morse_to_text(input_morse)
        print("Text:")
        print(text_result)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    while True: 
                main()