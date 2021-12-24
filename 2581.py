# 소수

import sys

input = sys.stdin.readline

prime = [True for _ in range(10001)]
prime[1]=False

for i in range(2,10001):
    k=2
    while True:
        if i*k>10000:
            break
        if prime[i*k] == True:
            prime[i*k] = False
        k+=1

m=int(input())
n=int(input())
ans=0
min_prime=-1
for i in range(n,m-1,-1):
    if prime[i] == True:
        min_prime = i
        ans+=i
if ans!=0:
    print(ans)
print(min_prime)