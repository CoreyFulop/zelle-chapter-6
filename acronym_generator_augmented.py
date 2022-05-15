# acronym_generator_augmented.py

def acronym(phrase):
    letters = []
    words_list = phrase.split()
    for word in words_list:
        letters.append(word[0].upper())
    return "".join(letters)
    
def main():
    print("This program produces an acronym from a phrase.\n")

    in_phrase = input("Enter your phrase: ")

    out_acronym = acronym(in_phrase)

    print(f"\nYour acronym is {out_acronym}.")

main()
