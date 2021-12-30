# DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

dict = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for i in range(1,n+1):
    dict[i].sort()

# print(dict)
visited_dfs=[False for _ in range(n+1)]
visited_bfs=[False for _ in range(n+1)]

dfs=[]
bfs=deque()
dfs.append(v)
bfs.append(v)
visited_bfs[v]=True

dfs_ans=[]
bfs_ans=[]
# print(dict)
while dfs:
    a = dfs.pop()
    if visited_dfs[a] == True:
        continue
    dfs_ans.append(a)
    visited_dfs[a] = True
    temp=sorted(dict[a],reverse=True)
    for i in temp:
        dfs.append(i)
    # print(dfs,dfs_ans)

# print(dfs_ans)

while bfs:
    a = bfs.popleft()
    bfs_ans.append(a)
    for i in dict[a]:
        if visited_bfs[i]==False:
            visited_bfs[i]=True
            bfs.append(i)

# print(bfs_ans)
print(' '.join(map(str,dfs_ans)))
print(' '.join(map(str,bfs_ans)))