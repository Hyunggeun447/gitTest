# 숨바꼭질 3

import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

dq = deque()

visited =[False for _ in range(100_001)]

dq.append([n,0])
visited[n] = True
while dq:
    #print(dq)
    [p,t]=dq.popleft()
    if p==k:
        print(t)
        break
    else:    
        if 2*p<100_001 and visited[2*p] == False and p<k:
            dq.appendleft([2*p,t])
            visited[2*p] = True
        if p+1<100_001 and visited[p+1] == False and p<k:
            dq.append([p+1,t+1])
            visited[p+1] =True
        if p-1>=0 and visited[p-1] == False:
            dq.append([p-1,t+1])
            visited[p-1] = True

