"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick the first element as a pivot.
Always pick the last element as a pivot (implemented below)
Pick a random element as a pivot.
Pick median as the pivot.
The key process in quickSort is a partition(). The target of partitions is, given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
"""
# Альтернативный метод, впоследствии получивший название «быстрая
# сортировка», изобрел информатик Чарльз Хоар в 1960. Он предполагает
# деление массива на две части, в одной из которых находятся элементы
# меньше определённого значения, в другой – больше или равные.
# Рассмотрим реализацию в Python быстрой сортировки Хоара.
nums = [4, 1, 6, 3, 2, 7, 8]

import random
# The choices() method returns a list with the randomly selected
# element from the specified sequence.

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_sums = []
        e_sums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_sums.append(n)
            else:
                e_sums.append(n)
        return quicksort(s_nums) + e_sums + quicksort(m_sums)

print(quicksort(nums))