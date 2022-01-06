# 분해합

import sys
input = sys.stdin.readline

n=int(input())

l=len(str(n))
# print(l)
k = n-9*l if n-9*l>0 else 0
for i in range(k,n):
    temp = i
    ans = i
    while temp>0:
        ans += temp%10
        temp=temp//10
    
    if ans == n:
        print(i)
        break
    elif i == n-1:
        print(0)