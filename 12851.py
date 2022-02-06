# 숨바꼭질 2

import sys
from collections import deque
input = sys.stdin.readline

n,k= map(int, input().split())

dq=deque()

dq.append(n)
check = [-1 for _ in range(100_001) ]

check[n]=0
count=0
while dq:
    x = dq.popleft()
    if x==k:
        count+=1
    for i in (x+1,x-1,x*2):
        if 0<= i <100_001:
            if check[i] == -1 or check[i]>=check[x]+1:
                check[i]=check[x]+1
                dq.append(i)

print(check[k])
print(count)