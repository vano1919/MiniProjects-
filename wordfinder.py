import json
from difflib import get_close_matches, SequenceMatcher

# Load the data from a JSON file into a dictionary
data = json.load(open("data.json"))

# Prompt the user and provide instructions for exiting
print("\nHi! if you want to exit, type-'exit' ")
print("By the way, 'exit' means: 'an act of going out of or leaving a place.'")

# Define a function to describe a word
def describe(w):
    # Declare the variable for the correctly spelled word
    global w_word
    # Check if the capitalized version of the word exists in the dictionary
    if w.capitalize() in data:
        w_word = w.capitalize()
        return data[w.capitalize()]
    # Check if the uppercase version of the word exists in the dictionary
    elif w.upper() in data:
        w_word = w.upper()
        return data[w.upper()]
    # Check if the lowercase version of the word exists in the dictionary
    else:
        w = w.lower()
    if w in data:
        w_word = w
        return data[w]
    # If the word is not found, suggest close matches
    elif get_close_matches(w, data.keys()):
        word_list = get_close_matches(w,data.keys())
        print("Wich word did you mean?")
        # List the close matches with their similarity ratio
        for index, item in enumerate(word_list,1):
            word = f"{index}. {item}"
            word_ratio = round(SequenceMatcher(None, w, item).ratio(),3)
            print(f"{word}, {word_ratio*100}%")

        # Ask the user to choose a close match
        while True:
            option = input("Please, choose option index: ")
            if option == "exit":
                print(f"{8*'_'}\n  Bye!\n{8*'_'}")
                break
            option = option.strip()
            # Ensure the user input is a number
            if not option.isnumeric():
                print("Please choose the number!" )
                continue
            # Ensure the user input is within the range of options
            if int(option) not in range(1,len(word_list)+1):
                print("Please choose correct range for index!")
                continue
            # Set the chosen option
            option = int(option) - 1
            break
        # Set the correctly spelled word to the chosen close match
        w_word = word_list[option]
        return data[word_list[option]]
    # If no close matches are found, inform the user
    else:
        print("\nThe word does not exist\n")
        if __name__ == "__main__":
            main()

# Define a main function to repeatedly prompt the user for words to describe
try:
    # Heading of the document
    with open("words.txt", "w", encoding="utf-8") as f:
        f.write(f"{50 * ' '}Words you searched for \n\n")
    def main():
        # Declare the variable for the correctly spelled word
        global w_word
        # Prompt the user for a word and check if they want to exit
        word = input("\nEnter a word to look up: ")
        while word == "exit":
            print(f"{55*'_'}\n{23*' '}Bye!\n search history is saved in the txt file named 'words' \n{55*'_'}")
            break
        else:
            # Describe the word and write the output to a file
            output = describe(word)
            with open("words.txt", "a", encoding="utf-8") as f:
                f.write(f"\nWord: {w_word}\n\n" )
            for index, item in enumerate(output, 1):
                print(f"{index}. {item}")
                with open("words.txt", "a", encoding="utf-8") as f:
                    f.write(f"\t{index}. {item}\n")
            if __name__ == "__main__":
                main()
    if __name__ == "__main__":
        main()
except:
    pass