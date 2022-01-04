# 부모의 트리찾기

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

search_parent = [0 for _ in range(n+1)]
search_parent[1]=1
dict ={i:[] for i in range(1,n+1)}

for _ in range(n-1):
    a, b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

temp = deque()
visited=[False for _ in range(n+1)]
temp.append(1)
visited[1] = True
# print(visited,temp,dict)
while temp:
    a = temp.popleft()

    for i in dict[a]:
        if visited[i] == False:
            search_parent[i]=a
            temp.append(i)
            visited[i] = True
        # print(visited,search_parent,temp)

for i in range(2,n+1):
    print(search_parent[i])






