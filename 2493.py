# 탑

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

ans=[]

towel=[]

for i in range(n):
    while towel:
        if towel[-1][1]>=lst[i]:
            ans.append(towel[-1][0]+1)
            break
        else:
            towel.pop()
    if len(towel)==0:
        ans.append(0)
    towel.append([i,lst[i]])
    # print(towel,ans)

print(" ".join(map(str, ans)))






