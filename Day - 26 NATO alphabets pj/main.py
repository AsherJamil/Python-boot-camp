

import pandas

data = pandas.read_csv("/python 100 days bootcamp/Github.git/Day - 26 NATO alphabets pj/nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
