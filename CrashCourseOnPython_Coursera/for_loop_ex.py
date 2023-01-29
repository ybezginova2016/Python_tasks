# 1
for x in range(5):
    print(x)

"""
1) In Python a range of numbers will start with
the value0 by default.

2) The list of numbers generated will be one
less than the given value.
"""
# 2
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print('Hi ' + friend)

# 3
values = [23, 52, 58, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print('Total sum: ' + str(sum)+ ' - Average: ' + str(sum/length))
print()

# 4
def to_celsius(x):
    return round((x-32)*5/9, 2)

for x in range(0, 101, 10):
    print(x, to_celsius((x)))

# TEST

# 2. Fill in the blanks to make the factorial function return the factorial
# of n. Then, print the first 10 factorials (from 0 to 9) with the
# corresponding number. Remember that the factorial of a number is
# defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120.
# Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,10):
    print(n, factorial(n))

# 3. Write a script that prints the first 10 cube numbers (x**3),
# starting with x=1 and ending with x=10.

for i in range(1, 11):
  print(i**3)

# 4. Write a script that prints the multiples of 7 between 0 and 100.
# Print one multiple per line and avoid printing any numbers that aren't
# multiples of 7. Remember that 0 is also a multiple of 7.

for i in range(0, 100):
    if i % 7 == 0:
        print(i)

# 5. The retry function tries to execute an operation that might fail,
# it retries the operation for a number of attempts. Currently, the code
# will keep executing the function even if it succeeds. Fill in the blank
# so the code stops trying after the operation succeeded.
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

######
print()
def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num += 1
        # (Fill in the missing line here)
    return max_num

print(find_max([4, 2, 5, 54]))
