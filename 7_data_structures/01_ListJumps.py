# def list_jumps(jumps):
#     # return the string 'cycle'  if the index will never leave the boundaries
#     # of the input list otherwise it must
#     # return 'out-of-bounds'. The starting index is always 0 .
#     res = 0
#     for k in jumps:
#         res = k + jumps[k]
#         if res in jumps:
#             print('cycle')
#         else:
#             print('out-of-bounds')


def list_jumps1(jumps):
    index = 0
    for _ in jumps:
        index = index + jumps[index]
        if index in jumps:
            print('cycle')
        else:
            print('out-of-bounds')

print(list_jumps1(6))

# print(list_jumps([1, 4, 3]))
"""
def findNumber(arr, k):
    if k in arr:
        return 'YES'
    else:
        return 'NO'

print(findNumber([3, 4, 5, 6, 11, 24, 22, 23, 2,], 6))
print(findNumber([3, 4, 5, 6, 11, 24, 22, 23, 2,], 7))
"""

