"""
Anagram

Given two strings, check whether two given strings are anagram of
each other or not. An anagram of a string is another string that
contains same characters, only the order of characters can be
different. For example, 'act' and 'tac' are anagrams of each other.

"""

# Hash Tables

input_str_1 = 'practice makes perfect'
input_str_2 = 'perfect makes practice'

input_str_3 = 'allergy'
input_str_4 = 'allergic'

def is_anagram(str_1, str_2):
    str_1 = str_1.replace(' ', '')
    str_2 = str_2.replace(' ', '')

    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    # creating two hash tables
    alphabet = 'abcdefghiklmopqrstuvwxyz'
    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1

# Is An Anagram? True or False
print(is_anagram(input_str_1, input_str_2))

# Is An Anagram? True or False
res_2 = is_anagram(input_str_3, input_str_4)
print(res_2)