# 설탕 배달

import sys
input = sys.stdin.readline

n = int(input())

ans=0

while True:
    if n%5 ==0:
        ans+=n//5
        print(ans)
        break
    elif n<0:
        print(-1)
        break
    else:
        n-=3
        ans +=1



