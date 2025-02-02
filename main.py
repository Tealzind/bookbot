def words_in_string(string):
    words = string.split()
    numberOfWords = 0

    for word in words:
        numberOfWords += 1

    return numberOfWords
    

def chars_in_string(chars):
    lowered_chars = chars.lower()
    characters = "abcdefghijklmnopqrstuvwxyz"
    char_dict = {}
    char_list_key = []
    char_list_value = []
    printList = []

    for char in characters:
        char_dict[char] = 0

    for char in lowered_chars:
        if char in char_dict:
            char_dict[char] += 1

    for char in char_dict:
        char_list_key.append(char)
        char_list_value.append(char_dict[char])

    print(char_list_key)
    print(char_list_value)

    for i in range(0, len(characters)):
        printList.append(f"The '{char_list_key[i]}' character was found {char_list_value[i]} times")

    return printList

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = words_in_string(file_contents)

        result = chars_in_string(file_contents)

        print(f"--- Begin report of {f.name} ---")
        print(f"{words} words found in the document")
        print()
        print(result)
        print("--- End report ---")
        

main()