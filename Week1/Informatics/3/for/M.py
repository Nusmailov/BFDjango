import functools
import math
cnt = 0
sum = 0
n = int(input())
for i in range (0,n):
    x = int(input())
    if x==0: cnt+=1
print(cnt)