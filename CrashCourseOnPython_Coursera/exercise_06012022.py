def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num +=1
        # (Fill in the missing line here)
        return max_num

print(find_max([4, 10, 3, 2]))