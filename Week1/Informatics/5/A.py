import functools
import math
cnt = 0
ans = -10000000
s = input().split(' ')
a = [int(i) for i in s]
b = a[0]
c = a[1]
d = a[2]
e = a[3]
def minim(e, b , c, d):
    ff = [e,b,c,d]
    ans = min(ff)
    return ans
print(minim(e,b,c,d))

#c = str(a)[::-1]
