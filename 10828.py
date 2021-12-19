# 스택

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

dq=deque()
for _ in range(N):
    list = input().rsplit()

    if list[0] == 'push':
        dq.append(int(list[1]))
    
    if list[0] == 'pop':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    if list[0] == 'size':
        print(len(dq))
    if list[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if list[0] == 'top':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

