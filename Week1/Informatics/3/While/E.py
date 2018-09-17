import functools
import math
cnt = 0
sum = 0
n = int(input())
t = 1
while t < n:
    t *= 2
    cnt += 1
print(cnt)
#c = str(a)[::-1]