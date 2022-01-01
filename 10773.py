# 제로

import sys
input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    k = int(input())
    if k == 0:
        lst.pop()
    else:
        lst.append(k)

print(sum(lst))