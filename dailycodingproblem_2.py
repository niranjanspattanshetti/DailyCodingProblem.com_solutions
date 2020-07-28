'''
   This problem was asked by Uber.
   Given an array of integers, return a new array such that
   each element at index i of the new array is the product of all the numbers
   in the original array except the one at i.
   For example,
   if our input was [1, 2, 3, 4, 5],
   the expected output would be [120, 60, 40, 30, 24].
   If our input was [3, 2, 1], the expected output would be [2, 3, 6].
   Follow-up: what if you can't use division?
'''
L = input("Enter the list: ").split()
M = []
for i in enumerate(L):
    L[i[0]] = int(i[1])
    M.append(int(i[1]))
for j in enumerate(L):
    L[j[0]] = 1
    for k in enumerate(M):
        if j[0] == k[0]:
            pass
        else:
            L[j[0]] = L[j[0]] * k[1]
print(L)
