import functools
import math
cnt = 0
sum = 0
n = int(input())
i = 2
while i < n + 1:
    if n % i == 0:
        print(i)
        break
    i+=1
#c = str(a)[::-1]
 
