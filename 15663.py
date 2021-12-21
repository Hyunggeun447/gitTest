# N과 M(9)

import sys
input = sys.stdin.readline

N , M = map(int, input().split())
lst = list(map(int, input().split()))
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
        if i not in visited and lst[i] != resently:
            list.append(lst[i])
            resently= lst[i]
            visited.append(i)
            dfs_back(start)
            list.pop()
            visited.pop()
            
dfs_back(0)