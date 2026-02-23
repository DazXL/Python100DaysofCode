"""
    This project is about converting a word into phonetic alphabet using Dictionary Comprehension extracting information
    from a CSV using pandas
"""
import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in data_frame.iterrows()}

word = input("Enter a word: ").upper()

output = [nato_alphabet[letter] for letter in word]
print(output)

