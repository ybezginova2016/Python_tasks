# An hour glass is made of 7 cells
# in following form.
#     A B C
#       D
#     E F G

# Approach:
# It is evident from the definition of the hourglass that the
# number of rows and number of columns must be equal to 3.
# If we count the total number of hourglasses in a matrix,
# we can say that the count is equal to the count of possible
# top left cells in an hourglass. The number of top-left cells
# in an hourglass is equal to (R-2)*(C-2). Therefore, in
# a matrix total number of an hourglass is (R-2)*(C-2).

# Python 3 program to find the maximum
# sum of hour glass in a Matrix

# Fixing the size of the Matrix.
# Here it is of order 6 x 6
R = 5
C = 5
# Function to find the maximum sum of hour glass
def maxSum(arr):
    # considering the matrix also contains
    max_sum = -50000

    # Negative values , so initialized with
    # -50000. It can be any value but very
    # smaller.
    # max_sum=0 -> Initialize with 0 only if your
    # matrix elements are positive

    if(R < 3 or C < 3):
        print("Not possible")
        exit()

    # Here loop runs (R-2)*(C-2) times considering
    # different top left cells of hour glasses.
    for i in range(0, R - 2):
        for j in range(0, C - 2):

            # Considering arr[i][j] as top
            # left cell of hour glass.
            SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

            # If previous sum is less
            # than current sum, then
            # update new sum in max_sum
            if (SUM > max_sum):
                max_sum = SUM
            else:
                continue

    return max_sum

arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]

print(maxSum(arr))