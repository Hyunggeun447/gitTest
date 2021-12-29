# 나이 순 정렬

import sys

input = sys.stdin.readline

n = int(input())
lst=[]

for _ in range(n):
    a, b = input().split()
    lst.append([int(a),str(b)])


lst.sort(key = lambda x:(x[0]))

for a,b in lst:
    print(a,b)