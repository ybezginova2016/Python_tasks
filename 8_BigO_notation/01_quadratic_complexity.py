# to remove unique elements from the result

def unique(l):
    res = []
    for e in l:                 # O(n)
        if e not in res:        # O(n) --> as a result O(n^2)
            res.append(e)
    return res

print(unique([5, 6, 3, 2, 1, 1, 1, 3, 7]))

# analysing the compextity list1, list2
def intersect(list1, list2):
    # initialise a temporary variable
    res = []
    # iterating over list1, list2
    for e1 in list1:            # n1
        for e2 in list2:        # n2 --> as a result n*n --> O(n^2)
            if e1 == e2:
                res.append(e1)
                break
    unique_res = unique(res) # + see O(n^2) from above
    return unique_res

# --> the Computational Complexity is O(n^2) + O(n^2) = 2*O(n^2) = O(2n^2) ~ O(n^2)

print(intersect([1, 4, 4, 5, 2, 13, 19], [8, 4, 3, 2, 1]))

