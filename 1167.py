# 트리의 지름

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph=[[] for _ in range(n+1)]


for _ in range(n):
    lst=list(map(int,input().split()))
    for i in range(1,len(lst)-2,2):
        graph[lst[0]].append((lst[i],lst[i+1]))

# print(graph)

def bfs(start):
    dq = deque()
    dq.append(start)
    check=[-1 for _ in range(n+1)]
    check[start] = 0
    max_l = 0
    max_p = start

    while dq:
        a = dq.popleft()
        for point, length in graph[a]:
            if check[point] == -1:
                check[point] = check[a]+length
                dq.append(point)
                max_l = max(max_l,check[point])
                if max_l == check[point]:
                    max_p = point
    return max_l,max_p

k=bfs(1)[1]
ans = bfs(k)[0]

print(ans)