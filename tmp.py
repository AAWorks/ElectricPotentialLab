from string import ascii_uppercase
import sys

class Analyze:
    def __init__(self, message):
        print(message)
        #self.message = message.upper()
        #elf.message_nospaces = self.message.replace(" ", "")
        #self.letter_count = len(message)
    
    def letter_frequency(self):
        self.freq_dict = {}
        for letter in ascii_uppercase:
            self.freq_dict[letter] = self.message.count(letter)
        return self.freq_dict

if __name__ == "__main__":
    Analyze(sys.argv()[1])