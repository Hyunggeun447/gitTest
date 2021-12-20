# N과 M(5)

import sys
input = sys.stdin.readline

N , M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)

list=[]

def dfs_back(start):
    if len(list) == M:
        print(' '.join(map(str,list)))
        return
    
    for i in range(start, N):
        if lst[i] not in list:
            list.append(lst[i])
            dfs_back(start)
            list.pop()

dfs_back(0)