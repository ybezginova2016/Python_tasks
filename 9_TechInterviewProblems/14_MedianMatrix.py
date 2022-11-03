"""
Given a N cross M matrix in which each row is sorted, find the overall
median of the matrix.

For example:

Matrix=
[1, 3, 5]
[2, 4, 6]
[3, 7, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5, so, we return 5.
"""
import numpy as np
A1 = np.array(
    [
        [1, 3, 5, 13],
        [2, 4, 6, 11],
        [3, 7, 9, 12]
    ]
)

print(A1)

# another option to define a matrix

l1 = [1, 3, 5]
l2 = [2, 4, 6]
l3 = [3, 7, 9]
A = [l1, l2, l3]

print(A)

def median_matrix(A):
    if len(A) == 1:
        vec = A[0]
        # getting a middle elements of the vec
        return vec[len(vec) // 2]
    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row]) # continuously building
        # return new_list
        new_list = sorted(new_list)
        # getting a middle elements of the vec
        return new_list[len(new_list)//2]

print(median_matrix(A))
print(median_matrix(A1))