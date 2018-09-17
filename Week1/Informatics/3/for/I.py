import functools
import math
cnt = 0
a = int(input())
dev = []
for i in range (1, int(math.sqrt(a)) + 1):
    if a%i==0:
        cnt+=1;
        if i*i!=0:
            cnt+=1;
print(cnt)
 
#c = str(a)[::-1]
 
