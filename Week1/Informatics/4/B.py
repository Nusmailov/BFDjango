import functools
import math
cnt = 0
sum = 0
n = int(input())
s = input().split(' ')
a = [int(i) for i in s]
for i in range (0,n):
    if  a[i]%2==0:
        print(a[i],end = ' ')
#c = str(a)[::-1]
 
