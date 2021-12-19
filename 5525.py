#  IOIOI

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input().strip())

#print(N, M, S)
ioi = 'I'
for _ in range(N):
    ioi+='OI'

answer = 0

for i in range(M-len(ioi)):
    if S[i] == 'I':
        if S[i:i+len(ioi)] == ioi:
            answer+=1
print(answer)