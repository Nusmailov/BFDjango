import functools
import math
cnt = 0
ans = -10000000
s = input().split(' ')
a = [int(i)for i in s]
x = a[0]
n = a[1]
def xor(x, n):
    return bool(x) ^ bool(n)
if xor(x,n):print(1)
else: print(0)
#a = [int(i) for i in s]
#c = str(a)[::-1]
