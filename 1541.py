# 잃어버린 괄호

import sys
input=sys.stdin.readline

N=str(input().rstrip())

num=N.rsplit('-')
answer=0
for i in range(0,len(num)):
    if '+' not in num[i]:
        temp_total=int(num[i])
    else:
        k=num[i].rsplit('+')
        for j in range(len(k)):
            k[j]=int(k[j])
        # print(k)
        temp_total=sum(k)
    if i==0:
        answer+=temp_total
    else:
        answer-=temp_total

print(answer)