"""
Given an array of integers, every element appears twice
except for one. Find that single one.

Note: Your algorithm should have a linear runtime
complexity. Could you implement it [without] using extra memory?

Example:
    Input: [1, 2, 2, 3, 1]
    Output: 3

{ element : number of occurences }

i = 0 {1 : 1}
i = 1 {1 : 1, 2 : 1}
i = 2 {1 : 1, 2 : 2}
i = 3 {1 : 1, 2 : 2, 3 : 1}
i = 4 {1 : 2, 2 : 2, 3 : 1}

XOR: b1 | b2
    0   0
    0   1
    1   0
    1   1
"""

def single_elem(arr):
    ans = 0
    for i in range(len(arr)):
        ans ^= arr[i]
    return ans

print(single_elem([1, 2, 2, 5, 3, 1]))

arr = [[1, 2, 4], [3, 5, 7, 9], [13]]
print(arr)
