import functools
import math
cnt = 0
sum = 0
n = int(input())
s = input().split(' ')
a = [int(i) for i in s]
ans = a[::2]
for i in ans:
    print(i, end = ' ')
#c = str(a)[::-1]
 