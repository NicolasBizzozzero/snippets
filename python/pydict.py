from re import findall, compile

def count_chars(string):
    char_dic = {}
    for char in string:
        if char in char_dic.keys():
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

def count_words(string):
    if not string:
        return {}

    regex = r"\b[a-zA-Z]+\b"
    regex = compile(regex)
    words_dic = {}

    return words_dic
    
def lower_chars_of_dict(dict):
    chars_to_lower = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    for char in chars_to_lower:
        if char in dict.keys():
            if char.lower() in dict.keys():
                dict[char.lower()] += dict[char]
            else:
                dict[char.lower()] = dict[char]
            del dict[char]
            
def upper_chars_of_dict(dict):
    chars_to_upper = "abcdefghijklmnopqrstuvwxyz"
    for char in chars_to_upper:
        if char in dict.keys():
            if char.upper() in dict.keys():
                dict[char.upper()] += dict[char]
            else:
                dict[char.upper()] = dict[char]
            del dict[char]
            
def delete_chars_from_dict(chars_to_delete, dict):
    for char in chars_to_delete:
        if char in dict.keys():
            del dict[char]

def delete_strings_from_dict(iterable_of_strings, dict):
    for string in iterable_of_strings:
        if string in dict.keys():
            del dict[string]


if __name__ == "__main__":
    dic = count_char("Coucou")
    print(dic)
    upper_chars_of_dict(dic)
    print(dic)
    delete_chars_from_dict("COaoO", dic)
    print(dic)