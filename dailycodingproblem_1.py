'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
import time
L = input("Enter the list:").split()
J = int(input('Enter the key:'))
for i in enumerate(L):
    L[i] = int(i[1])
for k in enumerate(L):
    for m in enumerate(L):
        if k[1]+m[1] == J:
            print 'True'
            time.sleep(3)
            exit()
        else:
            n = 1
if n == 1:
    print 'False'
