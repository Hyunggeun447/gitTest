
import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int, input().split())

level = [0 for _ in range(n+1)]
level[0] = -1

dq=deque()
dict={}
for i in range (1,n+1):
    dict[i]=[]

for _ in range(m):
    a,b = map(int, input().split())
    level[b]+=1
    dict[a]=[]
    dict[a].append(b)

for i in range(1,n+1):
    if level[i] == 0:
        dq.append(i)

ans = []

while dq:
    x= dq.popleft()
    ans.append(x)

    for i in dict[x]:
        level[i]-=1
        if level[i]==0:
            dq.append(i)


print(*ans)