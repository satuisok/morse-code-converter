import pandas as pd


class MorseConverter:
    def __init__(self):
        self.data = pd.read_csv("morse_code.csv")
        self.message = ""

        # Build dictionaries for faster lookup
        self.char_to_morse = dict(zip(self.data.character, self.data.morse_code))
        self.morse_to_char = dict(zip(self.data.morse_code, self.data.character))

    def encrypt(self):
        user_input = input("Enter your message: ").upper()
        converted_msg = ""

        for char in user_input:
            if char != " ":
                converted_msg += self.char_to_morse.get(char, "") + " "
            else:
                converted_msg += "/"

        self.message = ""
        self.message += converted_msg
        print(self.message)


    def decrypt(self):
        # Separate words to a list by using .split()
        morse_input = input("Enter your message. Use '/' as a separator: ").split("/")

        # Continue separating the letters of the word to a nested list
        elements = [word.split(" ") for word in morse_input]

        translation = []
        for word in elements:
            letters = ""
            for el in word:
                letters += self.morse_to_char.get(el, "")
            translation.append(letters)

        self.message = ""
        self.message += " ".join(translation)
        print(self.message)

    def start(self):
        while True:
            encrypt_decrypt = input("Type 'E' for encryption or 'D' for decryption. To exit, press 'Q': ").upper()

            if encrypt_decrypt == "Q":
                break
            elif encrypt_decrypt == "E":
                self.encrypt()
            elif encrypt_decrypt == "D":
                self.decrypt()
            else:
                print("Please try again.")


converter = MorseConverter()
converter.start()