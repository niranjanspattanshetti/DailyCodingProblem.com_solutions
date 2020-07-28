'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer
in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''
import time
L = input(" Enter the list: ").split()
for i in enumerate(L):
    L[i[0]] = int(i[1])
L.sort()
for i in range(0,max(L)+1):
    if i in L:
        pass
    else:
        print(str(i)+' is the first non negative integer not available in the list')
        time.sleep(2)
        exit()
