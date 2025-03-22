def count_words(text):
    word_list = []
    for word in text.split():
        word_list.append(word)
    num_words = len(word_list)
    return num_words

# solution code for above
# def get_num_words(text):
#     words = text.split()
#     return len(words)



def char_count(text):
    char_dict = {}
    for char in text.lower():
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

# solution code for above
# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

def sort_on(d):
    return d["num"]


def chars_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list