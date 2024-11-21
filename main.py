def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()















#From Boots-->

#def char_count(text):
 #   text = text.lower()
  #  counts = {}
   # for char in text:
    #    if char.isalpha():  # only count letters
     #       counts[char] = counts.get(char, 0) + 1
#    return counts  # return the dictionary instead of printing it

#def sort_on(dict_item):
 #   return dict_item["num"]

#def main():
 #   book_path = "books/frankenstein.txt"
  #  text = get_book_text(book_path)
   # num_words = get_num_words(text)
    
    #print("--- Begin report of books/frankenstein.txt ---")
    #print(f"{num_words} words found in the document\n")
    
    # Get the counts dictionary
    #counts = char_count(text)
    
    # Convert counts to list of dictionaries
    #characters = []
    #for char, count in counts.items():
     #   char_dict = {"char": char, "num": count}
      #  characters.append(char_dict)
    
    # Sort and print
    #characters.sort(reverse=True, key=sort_on)
    #for char_dict in characters:
     #   print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
