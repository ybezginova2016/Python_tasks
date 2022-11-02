# O(n^2)

def bubble(L):
    # (len(L)-1) passes
    for i in range(0, len(L) - 1):
        # with every pass, skip one last element that is already in order
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                # swap if the order is not right
                L[j], L[j+1] = L[j+1], L[j]


list1 = [1, 5, 0, 13, 2, 7, 5]
print(bubble(list1))