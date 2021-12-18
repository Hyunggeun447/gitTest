# 좌표압축

import sys
input = sys.stdin.readline

N = int(input())

lst=list(map(int, input().split()))
st=list(set(lst))
st=sorted(st)

dict={st[i]:i for i in range(len(st))}
 # print(dict)

answer=[]

for i in lst:
    answer.append(dict[i])

print(" ".join(map(str,answer)))
