import functools
import math
 
a = int(input())
for i in range(2, a+1):
    if a%i==0:
        print(i)
        break
 
#c = str(a)[::-1]