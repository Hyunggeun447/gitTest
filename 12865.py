# 배낭문제

import sys
input = sys.stdin.readline

n,k=map(int,input().split())

lst=[]

for _ in range(n):
    lst.append(list(map(int,input().split())))


check=[[0]*(k+1) for _ in range(n+1)]
# print(n,k,lst,check)

for i in range(1,n+1):
    for k in range(1,k+1):
        if lst[i-1][0]<=k:
            check[i][k]=max(check[i-1][k],lst[i-1][1]+check[i-1][k-lst[i-1][0]])
        else:
            check[i][k]=check[i-1][k]

print(check)