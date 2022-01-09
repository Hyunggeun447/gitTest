# 연속합

import sys
import math
input = sys.stdin.readline
INF = math.inf
n = int(input())

lst = list(map(int, input().split()))

ans = -INF
temp = 0
for i in lst:
    temp += i
    ans = max(ans,temp)
    if temp<0:
        temp = 0
    


print(ans)