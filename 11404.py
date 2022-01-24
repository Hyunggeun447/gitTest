# 플로이드

import heapq

import sys
import math
input = sys.stdin.readline

n=int(input())
m=int(input())
INF=math.inf

s= [[INF]*(n) for _ in range(n)]

for i in range(m):
    start, end, cost = map(int, input().split())
    if s[start-1][end-1]>cost:
        s[start-1][end-1] = cost


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j]>s[i][k]+s[k][j]:
                s[i][j]=s[i][k]+s[k][j]
            elif i==j:
                s[i][j]=0

for i in range(n):
    for j in range(n):
        if s[i][j]==INF:
            s[i][j]=0
    print(" ".join(map(str,s[i])))
