# 토마토
import sys
input=sys.stdin.readline

x , y = map(int, input().split())

tomato=[]
for _ in range(y):
    tomato.append(input().rsplit())


for i in range(x):
    for j in range(y):
        tomato[j][i]=int(tomato[j][i])
print(tomato)

k=2
while True:
    for i