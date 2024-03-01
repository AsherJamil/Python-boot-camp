import pandas

data = pandas.read_csv("/python 100 days bootcamp/Github.git/Day - 26 NATO alphabets pj/nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters are allowed")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()