# A -> B

import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

lst=deque()

a, b = map(int, input().split())

lst.append((b,1))
while lst:
    x,ans=lst.popleft()
    if x==a:
        print(ans)
        break
    elif x!=1 and x%10==1:
        lst.append((x//10,ans+1))
    elif x%2==0:
        lst.append((x//2,ans+1))
    else:
        print(-1)
        break
