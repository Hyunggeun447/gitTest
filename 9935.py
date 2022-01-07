# 문자열 폭팔

import sys
from collections import deque
input = sys.stdin.readline

string = str(input().strip())
bomb=str(input().strip())


check=[]

for k in string:
    check.append(k)
    if k == bomb[-1] and bomb == ''.join(check[-len(bomb):]):
        del check[-len(bomb):]

if len(check)>0:
    print(''.join(check))
else:
    print('FRULA')


