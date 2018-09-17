import functools
import math
cnt = 0
sum = 0
n = int(input())
i = 1
while i < n+1:
    if int(math.sqrt(i)) * int(math.sqrt(i)) == i:
        print(i)
    i+=1
