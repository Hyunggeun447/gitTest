# N과 M(12)

import sys
input = sys.stdin.readline

N , M = map(int, input().split())
lst = list(set(map(int, input().split())))
lst = sorted(lst)
# print(lst)
list=[]
visited = []
def dfs_back(start):
    if len(list) == M:
        print(' '.join(map(str,list)))
        return
    resently = 0
    for i in range(start, len(lst)):
        if lst[i] != resently:
            list.append(lst[i])
            resently= lst[i]
            visited.append(i)
            dfs_back(i)
            list.pop()
            visited.pop()
            
dfs_back(0)