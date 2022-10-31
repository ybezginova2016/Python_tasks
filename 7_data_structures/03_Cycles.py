# 3.5 - Cycles

# Consider a list of integer indices, indices. All elements of indices are
# within the bounds of the list indices. All the values in the list
# indices are unique. Example: [2, 0, 1, 4, 3, 5]

# Given an index, (e.g 0), move on to indices[0] (i.e 2 in the last example).
# Repeating that can be done indefinitely. A cycle occurs when a move returns
# to an already visited index. There is always at least one cycle. The sum of
# the lengths of the cycles is equal to the length of the list indices.

# Create a function cycles(indices) that returns a list of all cycles in indices.

# For the above example  [2, 0, 1, 4, 3, 5], the following is the expected output list:

# [[2, 0, 1], [4, 3], [5]]
# For the list [0, 1, 2, 3], the cycles are trivial and of the form:

# [[0], [1], [2], [3]]
# For [3, 2, 0, 1], there is a single cycle:

# [[3, 2, 0, 1]]
# Note: The order of the output cycles doesn't matter.
# [[2, 0, 1], [4, 3], [5]] would be equivalent to [[4, 3], [5], [2, 0, 1]].
# Additionally, order of the indices themselves don't matter either, so for
# example  [[2, 0, 1], [4, 3], [5]] is equivalent to [[0, 1, 2], [3, 4], [5]].