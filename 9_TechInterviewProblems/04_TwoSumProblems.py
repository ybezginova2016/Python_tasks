"""
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly
one solution, and you may not use the same element
twice.

Example:
    nums = [1, 2, 4, 6]
    target = 8
    --> to return the indices of 2 and 6

    8 - 1 = 7 -> {8: 0}
"""

### OPTION 1 ###
 # The first naive approach is to loop through the list,
 # sum of the given numbers in the list and compare the outcome
 # to the target value.
nums = [1, 2, 4, 6]
target = 8

def two_sum(nums, target):
    if len(nums) <= 1:
        return False
    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return[aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i


print(two_sum(nums, target))


