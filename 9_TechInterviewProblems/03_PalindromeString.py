"""
Given a string, write a function to determine
if is a palindrome.

FYI
Palindrome is a sequence of characters, which reads the same
from front to back.

"""
# Examples of polindromes:

# 'racecar'
# 'madam
#  'Dammit I'm mad.'

"""
To agree on:

1) we disregard the punctuation
2) we treat lower 'd' as an upper 'D'
3) we remove spaces
"""

import string
# importing a string module

def is_palindrome(s):
    # turn all the string to a lower case
    s = s.lower()

    # remove all the punctuation
    s = s.translate(string.punctuation)

    # remove white spaces with nothing ''
    s = s.replace(" ", "")
    # s = s.strip()

    return s == s[::-1]
    # s[::-1] - reverse

str_1 = "Dammit I'm mad."
str_2 = "racecar"
str_3 = "computer"

print(is_palindrome(str_1))
print(is_palindrome(str_2))
print(is_palindrome(str_3))