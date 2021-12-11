import sys

n=int(input())
stack=[0]
num=1
answer=[]
for i in range(n):
    k=int(sys.stdin.readline())
    while True:
        
        if stack[-1]==k:
            stack.pop()
            answer.append('-')
            break
        elif stack[-1]>k:
            answer.append('NO')
            break

        stack.append(num)
        num+=1
        answer.append('+')
    if answer[-1]=='NO':
        break

if answer[-1]=='NO':
    print('NO')
else:
    for i in answer:
        print(i)