# Given an array of comparable pbjects, you can find either min or the max
# of the elements in the array with n-1 comparisons, where n is the length of the array.

# Initialize values of min and max as minimum and maximum of the first
# two elements respectively. Starting from 3rd, compare each element
# with max and min, and change max and min accordingly (i.e., if the
# element is smaller than min then change min, else if the element
# is greater than max then change max, else ignore the element)

####### OPTION 1 #######
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()
    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    # If there are more than one element, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

# Time Compexity: O(n)
# Auxiliary Space: O(1)
print()
####### OPTION 2 #######
def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # if there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return arr_max, arr_min

    # if there are two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return arr_max, arr_min

    else:
        # if there are more than two elements
        mid = int((low + high) / 2)

        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

# Time Complexity: O(n)
# Auxiliary Space: O(log n)
# as the stack space will be filled for the maximum height of
# the tree formed during recursive calls same as a binary tree.