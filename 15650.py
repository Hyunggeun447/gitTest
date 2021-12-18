# N과 M(2)

import sys
input = sys.stdin.readline

N , M = map(int, input().split())

list=[]

def dfs_back(start):
    if len(list) == M:
        print(' '.join(map(str,list)))
        return
    
    for i in range(start, N+1):
        if i not in list:
            list.append(i)
            dfs_back(i+1)
            list.pop()

dfs_back(1)