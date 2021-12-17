# 마인크래프트

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

ground=[]

for _ in range(N):
    ground +=(input().rsplit())

for i in range(N*M):
    ground[i]=int(ground[i])

answer=float('inf')
for avr in range(257):
    B_temp=B
    high=0
    low=0
    # print(B_temp)
    for i in ground:
        if i < avr:
            low+=(avr-i)            
        else:
            high+=(i-avr)
    # print(time,B_temp)
    B_temp=B_temp+high-low
    if B_temp<0:
        continue
    time = 2*high + low
    if time <= answer:
        answer = time
        answer2=avr

print(answer, answer2)