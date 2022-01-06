# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

result = [1 for _ in range(n+1)]
for i in range(1,n):
    for j in range(i):
        if lst[j]<lst[i]:
            result[i]=max(result[i],result[j]+1)

print(max(result))