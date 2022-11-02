def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(arr))

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

# Time Complexity: O(N2)
# Auxiliary Space: O(1)


nums = [4, 1, 6, 3, 2, 7, 8]
n = 1
while n < len(nums):
   for i in range(len(nums) - n):
       if nums[i] > nums[i + 1]:
           nums[i], nums[i + 1] = nums[i + 1], nums[i]
   n += 1

print('\n', nums)

# Однако на практике он неэффективен, так как предполагает
# многократное прохождение по всему массиву.
