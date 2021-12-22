# 좌표 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

lst=sorted(lst, key=lambda x:(x[0],x[1]))

for i in range(len(lst)):
    print(" ".join(map(str, lst[i])))