
import functools
import math
cnt = 0
sum = 0
n = int(input())
s = input().split(' ')
a = [int(i) for i in s]
for i in range (1, n):
    if  (a[i] > 0 and a[i-1] > 0) or(a[i] < 0 and a[i-1] < 0):
        cnt+=1
 
if cnt > 0: print("YES")
else: print("NO")
#c = str(a)[::-1]