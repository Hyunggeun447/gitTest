# 용액

from operator import ne
import sys
import math

input = sys.stdin.readline
INF = math.inf
n = int(input())

lst= list(map(int, input().split()))

# print(n,lst)

i=0
j=len(lst)-1

min_ans=INF
ans=[0,0]

while i<j:
    sol1=lst[i]
    sol2=lst[j]

    sum_sol=sol1+sol2

    if abs(sum_sol)<min_ans:
        min_ans = abs(sum_sol)
        ans[0]=sol1
        ans[1]=sol2


    if sum_sol>0:
        j-=1

    else:
        i+=1

print(ans[0],ans[1])

