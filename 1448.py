# 삼각형 만들기

import sys
input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    lst.append(int(input()))

lst = sorted(lst, reverse=True)

# print(lst)

for i in range(n-2):
    if lst[i]<lst[i+1]+lst[i+2]:
        print(lst[i]+lst[i+1]+lst[i+2])
        break
    elif i==n-3:
        print(-1)