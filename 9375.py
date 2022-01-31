# 패션왕 신해빈

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    dict={}
    check=[]
    for _ in range(m):
        a,b=map(str,input().split())
        if b not in dict:
            dict[b]=[]
            check.append(b)

        dict[b].append(a)
    if len(check) == 1:
        print(len(dict[check[0]]))
    else:
        ans=1
        for i in range(len(check)):
            ans=ans*(1+len(dict[check[i]]))
        print(ans -1)

