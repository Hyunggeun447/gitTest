# 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

lst_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for j in range(1,n+1):
    for i in range(1,n+1):
        lst_sum[j][i] = lst[j-1][i-1] + lst_sum[j-1][i] + lst_sum[j][i-1] - lst_sum[j-1][i-1]



for _ in range(m):
    y1,x1,y2,x2 = map(int, input().split())
    ans = lst_sum[y2][x2] - lst_sum[y1-1][x2] - lst_sum[y2][x1-1] + lst_sum[y1-1][x1-1]
    print(ans)