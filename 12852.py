#  1로 만들기 2 

import sys
input = sys.stdin.readline
from collections import deque

n=int(input())

dq=deque()
visited=[False for _ in range(1_000_001)]
dq.append((n,0,[n]))
visited[n]=True
answer=1_000_00110

while dq:
    n, k, list = dq.popleft()
    if k<answer:
        if n==1:
            answer=k
            answer_2=list
        else:
            if n%3==0 and visited[n//3]==False:
                n_new = n//3
                visited[n//3]=True
                dq.append((n_new,k+1,list+[n//3]))
            if n%2==0 and visited[n//2]==False:
                n_new = n//2
                visited[n//2]=True
                dq.append((n_new,k+1,list+[n//2]))
            if n>1 and visited[n-1]==False:
                visited[n-1]=True
                dq.append((n-1,k+1,list+[n-1]))

print(answer)
print(" ".join(map(str,answer_2)))