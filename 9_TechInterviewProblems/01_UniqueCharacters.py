"""
Implement an algorithm to determine if a string has all unique
characters.

UPD: Let's consider specific strings
1) 'unique' - 'u' appears twice? --> False
2) 'bear' - indeed unique? --> True
"""
s1 = 'unique'
s2 = 'bear'

#### OPTION 1 - EASIEST ####
# set() function returns a unique elements only
print(set(s1))
print(set(s2))

# so, having an idea about set(), we can check whether
# the len(string) == len of the set()

def is_unique(s):
    return len(s) == len(set(s))

print(is_unique('Luxoft'))
print(is_unique('bear'))
print(is_unique('unique'))