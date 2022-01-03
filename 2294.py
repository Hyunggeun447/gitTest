# 동전 2

import sys
import math
input = sys.stdin.readline
INF = math.inf

n , k = map(int, input().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))
coins=list(set(coins))
coins.sort()

# print(coins)

num =[INF for _ in range(k+1)]
num[0]=0
for coin in coins:
    for i in range(coin,k+1):
        num[i] = min(num[i],num[i-coin]+1)

if num[k] != INF:        
    print(num[k])
else:
    print(-1)
