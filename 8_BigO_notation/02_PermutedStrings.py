# 4.2 - Permuted Strings
# Check if strings are permutations of each other

# Write a function that will determine if two strings are permutations
# of each other. A permutation is the result of an ordering operation
# done on a collection of items (in this case, characters in the string.) is_permutation(str1, str2) returns a boolean.

# Determine Permutation

# A permutation list p applied to s creates a new string t, where
# t[i] = s[p[i]]. For example, when p = [2, 0, 1], it transforms
# abc into cab.
# Given strings a and b, where b is a permutation of a:
# Find a permutation list that when applied to a will return b.

# get_permutation_list(str1, str2):

# Examples:
# get_permutation_list(["ABC", "ABC"] == [0, 1, 2]
#   get_permutation_list(["ABC", "CAB"] == [2, 0, 1]
# You can assume that get_permutation_list will receive two
# strings that are permutations of each other.

# Is it a Permutation?
# 'the cow jumps over the moon.'
# 'the moon jumps over the cow.' <- Permutation

string_1 = 'driving'
string_2 = 'drivign'

def is_permutation(string_1, string_2):
    # removing spaces
    # string_1 = string_1.replace(' ', '')
    # string_2 = string_2.replace(' ', '')

    string_1 = string_1.strip()
    string_2 = string_2.strip()

    if len(string_1) != len(string_2):
        return False

    # looping to check if the character from the string_1 is present in the string_2
    for c in string_1:
        if c in string_2:
            # remove the character with nothing ''
            string_2 = string_2.replace(c, '')
    return len(string_2) == 0

print(is_permutation(string_1, string_2))