# 특정한 최단 경로
# 다익스트라를 활용한 최단경로 구하기
# 공부해야할 것

import sys
input = sys.stdin.readline
from collections import deque
import heapq
import math

N , E = map(int, input().split())

graph={i:{} for i in range(1,N+1)}



for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b]=c
    graph[b][a]=c

#print(graph)

v1 , v2 = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {vertex : [float('inf'), start] for vertex in graph}
    distances[start] = [0,start]

    queue=[]
    heapq.heappush(queue, [distances[start][0],start])

    while queue:
        now_distance, now_vertex = heapq.heappop(queue)

        if distances[now_vertex][0]<now_distance:
            continue
        for adjacent, weight in graph[now_vertex].items():
            distance = now_distance + weight
            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, now_vertex]
                heapq.heappush(queue, [distance, adjacent])
    return (distances[end][0])            

path1 = dijkstra(graph,1,v1) +dijkstra(graph,v1,v2) + dijkstra(graph,v2,N)
path2 = dijkstra(graph,1,v2) + dijkstra(graph,v2,v1) + dijkstra(graph,v1,N)

answer= min(path1,path2)

if math.isinf(answer):
    print(-1)
else:
    print(answer)