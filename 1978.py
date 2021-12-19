# 소수 찾기
import sys
input = sys.stdin.readline

N = int(input())

list = list(map(int, input().split()))

prime=[True for _ in range(1001)]
prime[0] = False
prime[1] = False
for i in range(2,1001):
    k=2
    if prime[i] == False:
        continue

    while k*i<1001:
        prime[k*i] = False
        k+=1

answer = 0
for i in list:
    if prime[i] == True:
        answer+=1

print(answer)