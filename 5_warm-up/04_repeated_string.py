##### Repeated String ######

# There is a string, s, of lowercase English letters that is
# repeated infinitely many times. Given an integer, n, find and
# print the number of letter a's in the first  letters of the
# infinite string

# Function Description
# Complete the repeatedString function in the editor below.
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider

# Returns
# int: the frequency of a in the substring

#### OPTION 1 ####
def repeatedString(s, n):
    # s: a string to repeat
    # n: the number of characters to consider
    s = s.lower()
    n_s = len(s)
    count = s.count('a')
    count = count * (n//n_s)
    for i in range(n%n_s):
        if s[i]=='a':
            count += 1
    return count

print(repeatedString('aaaabcaaaefb', 323))

#### OPTION 2 ####
def rep_string(s, n):
    return (n//len(s)*s.count('a') + s[:n%len(s)].count('a'))
print(rep_string('naaandvbaaa', 190))
