from math import sqrt
import functools
from decimal import *
import math
n = int(input())
mp = {}
arr = []
nm = []
mx = 10010100
for i in range(0, n):
    name = input()
    score = float(input())
    mp[name] = score
    arr.append(score)
    nm.append(name)
    mx = min(mx, score)
arr = sorted(arr)
for i in range(0, len(arr)):
    if mx < arr[i]:
        mx = arr[i]
        break;

nm = sorted(nm)
#for i in range(0, len(nm)):
#    print(nm[i])

for i in range(0, len(nm)):
    if mp[nm[i]] == mx:
        print(nm[i])
#print("{0:.2f}".format(mp[str(t)]))