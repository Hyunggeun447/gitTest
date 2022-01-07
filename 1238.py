# 파티

import sys
import math
import heapq
input = sys.stdin.readline
INF = math.inf
n, m, x = map(int, input().split())

way = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a,b,c = map(int,input().split())
    way[a].append([b,c])

def dijkstra(s,e):
    length = [INF]*(n+1)
    length[s]=0
    hp=[]
    heapq.heappush(hp,[0,s])

    while hp:
        [l_now, point_now] = heapq.heappop(hp)
        if length[point_now]<l_now:
            continue

        for p,l in way[point_now]:
            if length[p]>l+l_now:
                heapq.heappush(hp,[l+l_now,p])
                length[p]=l+l_now
    
    
    return length[e]

ans=0
for i in range(1,n+1):
    ans=max(dijkstra(x,i)+dijkstra(i,x),ans)
print(ans)



