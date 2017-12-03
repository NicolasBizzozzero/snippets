# To use regex with Python3, we have to import re.
import re

Regex_Pattern = r"_________" # This variable is our regular expression, we have to keep the r at the beggining, we juste have to modify the "_________" part.
Test_String = "This is a test String. We're gonna look for stuff in here with our Regular Expression."
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# This regexp match every word containing "coucou".
Regex_Pattern = r"coucou"

# The dot '.' can replace every character except for the newline character.
# This regexp match every word containing 3 characters.
Regex_Pattern = r"..." 

# You can escape the rule above by typping '\.' if you're looking for the character '.'.
# This regexp match every word with the patern "xxx.xxx.xxx.xxx", with x being any character.
Regex_Pattern = r"...\....\....\...." 

# The "\d" expression match any digit between 0 and 9.
# The "\D" expression match any character that is not a digit.
# This regexp match every word with the patern "aaXaaXaaaa", with X being any character who is not a digit, and a any digit.
# This can be usefull if you're looking for a date.
# This can match : "06-11-2015"
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"

# The "\s" expression match any whitespace character {\r, \n, \t, \f}.
# The "\S" expression match any character that is not a whitespace character.
# This regexp match every word with the patern "XXaXXaXX", with X being any character who is not a whitspace, and a whitespace character.
Regex_Pattern = r"\S\S\s\S\S\s\S\S"

# The "\w" expression match any word character {a-z, A-Z, 0-9, _}.
# The "\W" expression match any character that is not a word character.
# This regexp match every word with the patern "aaaXaaaaaaaaaaXaaa", with X being any non-word character, and a any word-character.
# This can match : "www.hackerrank.com"
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"

# The "^abc" expression match any string starting with "abc".
# The "abc$" expression match any string finishing with "abc".
# This regexp match every word with the patern "daaaa.", with d being a digit and a being any word character. These words 'll finish by a dot and have a size of 6.
# This can match : "0qwer."
Regex_Pattern = r"^\d\w\w\w\w\.$"

# The "[aeiouy] est une voyelle." expression match any string starting with {a, e, i, o, u, y} and finishing with " est une voyelle.".
# The "[^aeiouy] n'est pas une voyelle." expression match any string NOT starting with {a, e, i, o, u, y} and finishing with " n'est pas une voyelle.".
# A hyphen '-' inside a character class "[]" specify a range of characters.
# [4-8] = [45678], [a-d] = [abcd], [A-D] = [ABCD].
Regex_Pattern = r"[aeiouy] est une voyelle."
Regex_Pattern = r"[^aeiouy] n'est pas une voyelle."

# The "^[1-3]{3}$" expression match any string of length 3 containing only 1, 2 or 3.
# The "^[1-3]{3,}$" expression match any string of length of at least 3 containing only 1, 2 or 3.
# This regexp match every word starting with the patern "www."
# This can match : "www.wikipedia.com"
Regex_Pattern = r"^w{3}\."

# The "^[0-9]*$" expression match any string containing only digits, of length 0 or more.
# The "^[0-9]+$" expression match any string containing only digits, of length 1 or more.
Regex_Pattern = r"^[0-9]*$"
Regex_Pattern = r"^[0-9]+$"

# "\b" serve as an anchor to mark word boundaries. You can use it to match words like this "\bword\b".
# For example, the regexp "\bcat\b" in the sentence "The cat scattered his food all over the room." will  match the word "cat" but not the "cat" in "scattered".
# "\B" serve as an anchor to mark NON-word boundaries. You can use it to match stuff inside words like this "\Bor\B".
# For example, the regexp "\B.\B" will match every character not at a word boundary. In "abcde", it'll match 'b', 'c' and 'd'.
# This regexp match every lowercase word starting with a vowel.
Regex_Pattern = r"\b[aeiouy][a-Z]\b"

# The parenthesis can group part of regexp together. You can then apply quantifier at theses groups.
# This regexp match every string containing 3 or more repetitions of "ok".
Regex_Pattern = r'(ok){3,}'

# The question mark can make a part of a regex optionnal.
# For example, "colou?r" will match both "color" and "colour". 
Regex_Pattern = r'coulou?r'

# the vertical line '|' serve as a logical or.
# "(Bob|Kevin|Stuart)" will match "Bob" or "Kevin" or "Stuart".
Regex_Pattern = r'(Bob|Kevin|Stuart)'

# "\1" references the first capturing group, "\2" the second etc.
# This regexp match every number with the two same digits and of length 2.
# This can match : "00", "11", "22", "33" ...
Regex_Pattern = r'^(\d)\1?'

# The positive lookahead regex1(?=regex2) match regex1 if regex1 is immediatly followed by regex2.
# The negative lookahead regex1(?!regex2) match regex1 if regex1 is NOT immediatly followed by regex2.
# The positive lookbehind (?<=regex2)regex1 match regex1 if regex1 is immediatly preceded by regex2.
# The negative lookbehind (?<!regex2)regex1 match regex1 if regex1 is NOT immediatly preceded by regex2.
# This regexp match every occurences of "oui" followed immediatly by "stiti".
Regex_Pattern = r'oui(?=stiti)'












"""

import re

def evaluer(str):
    regex_commence = r'^hackerrank'
    regex_termine = r'[\w\s]*\bhackerrank\b$'
    regex_commence = re.compile(regex_commence)
    regex_termine = re.compile(regex_termine)
    
    if regex_commence.match(str):
        if regex_termine.match(str):
            return 0
        else:
            return 1
    elif regex_termine.match(str):
        return 2
    else:
        #print(str)
        return -1
    
for i in range(input()):
    print(int(evaluer(raw_input())))

"""

"""

import re

def evaluer(str):
    regex = r'hackerrank'
    regex = re.compile(regex)
    
    if re.findall(regex, str):
        return True
    else:
        return False
    
counter = 0    
for i in range(input()):
    if evaluer(raw_input()):
        counter += 1

print(counter)

"""

"""

import re

def evaluer(str):
    regex = r'hackerrank'
    regex = re.compile(regex)
    
    result = re.split("[- ]", str)
    return result[0], result[1], result[2]
        
for i in range(input()):
    result = evaluer(raw_input())
    print('CountryCode={cc},LocalAreaCode={lac},Number={n}'.format(cc=result[0], lac=result[1], n=result[2]))

"""