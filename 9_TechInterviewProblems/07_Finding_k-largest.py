"""
FIND THE kTH LARGEST ELEMENT

Many algorithms require as a subroutine the computation of the
kth largest element of an array. The
first largest element is simply the largest element.
The nth largest element is the smallest element,
where n is the length of the array.

For example:

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
Output: 10
"""

def k_largest(arr, n, k):
    return arr[k+2]

arr = [12, 3, 5, 7, 19]
n = len(arr)
k = 2

print("K'th largest element is", k_largest(arr, n, k))

# Approach 1: Sort
# The most naive approach to solve this problem is to simply
# sort the given array in descending order and return the
# Kth element from the beginning of the array.
def kthLargest(arr, k):
    arr = sorted(arr, reverse=True)
    return arr[k - 1]

print(kthLargest([1, 42, 66, 4, 15], 2))

# Approach 2: Heap
# The previous approach of sorting and finding the Kth largest
# element is costly. Since the task is to return the Kth largest
# element, the idea would be to maintain a data structure that
# keeps the elements of the array in sorted order, along with
# reducing the time complexity.

# The idea is to use a max-heap. Since max-heap keeps all the
# elements in sorted order, the problem simply converts
# to print the Kth element of the max-heap.

def countSwaps(a):
    numSwap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwap += 1

    print('Array is sorted in', numSwap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[len(a) - 1])

def countSwaps2(a):
    # Write your code here
    length = len(a)
    swap_count = 0
    for i in range(length - 1):
        for j in range(length - 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                swap_count += 1
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

print(countSwaps2([1, 42, 66, 4, 15]))


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]