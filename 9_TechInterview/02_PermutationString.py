
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