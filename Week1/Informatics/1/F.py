from math import sqrt
import functools
import math
n = int(input())
mp = {}
for i in range(0, n):
    s = input().split(' ')
    mp[str(s[0])] = round((round(float(s[1]), 2) + round(float(s[2]), 2) + round(float(s[3]),2)), 2)/3
t = input()
print(round(float(mp[str(t)]), 2))

#a = [int(i) for i in s]
#c = str(a)[::-1]
