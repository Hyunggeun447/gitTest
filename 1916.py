# 최소비용 구하기

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    
dp=[INF for _ in range(n+1)]
start, end = map(int, input().split())



def dijkstra(start):
    heap=[]
    dp[0], dp[start] = 0, 0
    heapq.heappush(heap,(0,start))

    while heap:
        dist, now = heapq.heappop(heap)

        if dp[now] < dist:
            continue
        
        for next_node, temp_dist in graph[now]:
            next_dist=temp_dist+dist

            if next_dist < dp[next_node]:
                dp[next_node] = next_dist
                heapq.heappush(heap,(next_dist,next_node))
    #print(dp)
    return 
dijkstra(start)
print(dp[end])