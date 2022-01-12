# Four Squares


import sys
import math
input = sys.stdin.readline

n = int(input())

ans = 0
while n > 0:
    i=int(math.trunc(n **0.5))
    n -= i**2
    ans+=1
    print(n,i,ans)

print(ans)
