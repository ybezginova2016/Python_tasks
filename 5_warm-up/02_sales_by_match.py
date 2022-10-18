###### PAIRING SOCKS ######

# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# Example
# There is one pair of color  and one of color . There are three odd socks left, one of each color.
# The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below.
#
# sockMerchant has the following parameter(s):
#
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns
#
# int: the number of pairs
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the
# socks in the pile.

def sockMerchant(n, ar):
    # Write your code here
    kvs = []
    a = {}
    for i in ar:
        a[i] = ar.count(i)

    a_val = list(a.values())
    for i in a_val:
        kvs.append(i // 2)

    return sum(kvs)

print(sockMerchant(13, [1, 2, 1, 3, 2, 2, 1, 2, 3]))