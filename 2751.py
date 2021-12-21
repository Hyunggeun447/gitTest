# 수 정렬하기2

import sys
input = sys.stdin.readline

n = int(input())

lst=[]

for _ in range(n):
    lst.append(int(input()))

lst=sorted(lst)

for i in lst:
    print(i)