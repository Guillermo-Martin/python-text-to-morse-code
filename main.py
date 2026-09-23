# morse code dictionary
MORSE_CODE = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": ".._.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "0": "-----",
  " ": "/"
}

# variable to hold the morse code
converted_text = ""

# ask user for a text to convert
text_to_convert = input("Enter text to convert: ").lower()

# loop through each character in the text
for char in text_to_convert:
  converted_text += MORSE_CODE[char]

  # add space between letters so it's more readable
  converted_text += " "

# show final message
# "[:-1]" removes the last space from the string
print(f"Here's the Morse Code for your text: {converted_text[:-1]}")
