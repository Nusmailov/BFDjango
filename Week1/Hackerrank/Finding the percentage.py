from math import sqrt
import functools
from decimal import *
import math
n = int(input())
mp = {}
for i in range(0, n):
    s = input().split(' ')
    mp[str(s[0])] = (float(s[1]) + float(s[2]) + float(s[3]))/3
t = input()
print("{0:.2f}".format(mp[str(t)]))