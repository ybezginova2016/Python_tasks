# List Comprehension
# newlist = [expression for item in iterable if condition == True]

# List comprehension offers a shorter syntax when you want to
# create a new list based on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list, containing only
# the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement
# with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# With list comprehension you can do all that with only
# one line of code:
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]
newlist2 = [x for x in fruits if x != "apple"]

print(newlist1)
print(newlist2)

newlist3 = [x for x in range(10) if x < 5]
print(newlist3)

newlist4 = [x for x in range(10)]
print(newlist4)

newlist5 = [x if x != "banana" else "orange" for x in fruits]
print(newlist5)

newlist6 = ['hello' for x in fruits]
print(newlist6)