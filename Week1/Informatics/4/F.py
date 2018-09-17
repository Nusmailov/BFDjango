import functools
import math
cnt = 0
sum = 0
n = int(input())
s = input().split(' ')
a = [int(i) for i in s]
for i in range (1, n - 1):
    if a[i] > a[i-1]  and a[i] > a[i+1]:
        cnt+=1
print(cnt)
#c = str(a)[::-1]
 
