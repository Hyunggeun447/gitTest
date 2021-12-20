# 카드2

import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

lst = [i for i in range(1,n+1)]
lst=deque(lst)
# print(lst)
toggle = True
while len(lst)>1:
    if toggle == True:
        lst.popleft()
        toggle = False
    else:
        temp = lst.popleft()
        lst.append(temp)
        toggle = True

print(lst[0])


