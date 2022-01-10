# 포도주 시식(dp)

import sys
input = sys.stdin.readline

n = int(input())

lst=[]

for _ in range(n):
    lst.append(int(input()))

dp=[]
if n>2:
    dp.append(lst[0])
    dp.append(lst[1]+lst[0])
    dp.append(max(lst[2]+lst[0],lst[2]+lst[1],dp[1]))
    for i in range(3,len(lst)):
        dp.append(max(lst[i]+dp[i-2],lst[i]+lst[i-1]+dp[i-3],dp[i-1]))
    print(max(dp))
else:
    print(sum(lst))