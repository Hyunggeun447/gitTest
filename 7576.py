# 토마토

import re
import sys
from collections import deque

input = sys.stdin.readline

m , n = map(int, input().split())
lst= [list(map(int, input().split())) for _ in range(n)]

dq = deque()

dx , dy = [-1,1,0,0] , [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            dq.append([i,j])

def tomato():
    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y]+1
                dq.append([nx,ny])

ans = 0
tomato()
for i in lst:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    
    ans= max(ans,max(i))

print(ans-1)
