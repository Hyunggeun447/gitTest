# 수 정렬하기 3

import sys
input = sys.stdin.readline

n = int(input())

lst=[0 for _ in range(100_000)]

for _ in range(n):
    k= int( input())
    lst[k]+=1

for i in range(100_000):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)