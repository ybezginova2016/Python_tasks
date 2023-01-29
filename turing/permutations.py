# A Python program to print all
# permutations using library function
from itertools import permutations
import random

# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

# Print the obtained permutations
for i in list(perm):
    print(i)


# Get all permutations of length 2
# and length 2
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
    print(i)

# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 character

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)

print()
def perm(a, k=0):
   if k == len(a):
      print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i], a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

print(perm([1,2,3]))
print('Turing')
print('Option 1 - False')
# Get all permutations of length 2
# and length 2
perm = permutations([[1,2,3,4], [4,3,1,2]], 2)
# Print the obtained permutations
for i in list(perm):
    print(i)

print('Option 2 - True')
perm = permutations([1,2,3,4], 2)
# Print the obtained permutations
for i in list(perm):
    print(i)

print('Solution')

def get_samples(n, m, k):
    """
    n - кол-во элементов
    m - сколько отбираем за раз
    k - число выборок
    """
    samples = []
    # исходный массив
    alist = range(1, n+1)
    # k раз делаем выборки:
    for _ in range(k):
        sample = random.sample(alist, m)
        samples.extend(sample)
    # делаю сет из листа (в сете остаются только уникальные элементы)

    set_sam = set(samples)
    if len(samples) == len(set_sam):
        return 'unique'
    else:
        return 'not_unique'

results = dict(unique=0, not_unique=0)

N = 10000

for _ in range(N):
    results[get_samples(10, 2, 3)] += 1

print(float(results['unique'])/N)

print()
def copy(arr):
    res=[]
    for a in arr:
        res.append(a)
    return res

def perms(n):
    if (n==1):
        return [[1]]
    else:
        tmp=perms(n-1)
        res=[]
        for p in tmp:
            for i in range(len(p)+1):
                pp=copy(p)
                pp.insert(i, n)
                res.append(pp)
        return res

def perms_of_list(alist):
    n=len(alist)
    tmp=perms(n)
    res=[]
    for p in tmp:
        pp=[]
        for i in p:
            pp.append(alist[i-1])
        res.append(pp)
    return res

print(perms_of_list(['a', 'b', 'c']))

print()
def solution(n: int, m: int, games):

   pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

   for round in games:
       for i, j in pairs:
           if i in round[:n // 2] and j in round[:n // 2]:
               return False
           if i in round[n // 2:] and j in round[n // 2:]:
               return False
   return True

if __name__ == '__main__':
    print(solution(2, 1, [[1, 2]]))
    print(solution(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
    print(solution(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))
    print(solution(6, 6, [[1,6,3,4,5,2],[6,4,2,3,1,5],[4,2,1,5,6,3],[4,5,1,6,2,3],[3,2,5,1,6,4],[2,3,6,4,1,5]]))
    print(solution(6, 6, [[3,1,4,5,6,2],[5,3,2,4,1,6],[5,3,6,4,2,1],[6,5,3,2,1,4],[5,4,1,2,6,3],[4,1,6,2,5,3]]))
"""
Explanation:

To solve this problem, you can create a list of pairs of players and 
initialize it with all pairs of players. Then, for each round of games, 
you can iterate through the players and check if they have played 
against each other. If they have, you can remove the pair from the 
list. At the end, you can return whether the list is empty or not.
"""

print('Solution 2')
def solution2(n: int, m: int, games):
    command = int(n / 2)

    for i in range(m-1):
        for j in range(0, n, command):
            ll = []
            for p in range(command):
                ll.append(games[i][j+p])

            for ii in range(i+1, m):
                for jj in range(0, n, command):
                    ll2 = []
                    for p in range(command):
                        ll2 = []
                        ll2.append(games[ii][jj+p])
                    if ll == ll2:
                        return False
    return True


if __name__ == '__main__':
    print(solution2(2, 1, [[1, 2]]))
    print(solution2(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
    print(solution2(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))
    print(solution2(6, 6, [[1,6,3,4,5,2],[6,4,2,3,1,5],[4,2,1,5,6,3],[4,5,1,6,2,3],[3,2,5,1,6,4],[2,3,6,4,1,5]]))
    print(solution2(6, 6, [[3,1,4,5,6,2],[5,3,2,4,1,6],[5,3,6,4,2,1],[6,5,3,2,1,4],[5,4,1,2,6,3],[4,1,6,2,5,3]]))
