# R-1.2 Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return True if k[-1] == 0 or 2 or 4 or 6 or 8 else False

k = input('Please enter k: ')

result = is_even(list(k))
print('True :)') if result is True else print('False!')



def is_even2(k):
    # bitwise-and
    # 1 & 1 = 1 odd, 0 & 1 = 0 even
    return False if k & 1 else True

print(is_even2(76))
