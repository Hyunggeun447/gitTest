# 파이프 옮기기1
import sys
input= sys.stdin.readline

n= int(input())

lst=[]

for _ in range(n):
    temp=list(map(int,input().split()))
    lst.append(temp)

# print(lst)

now_x,now_y = 0 , 1
dirc='right'

answer=0
def pipe(x,y,dirc):
    #print(x,y,dirc)
    if x == n-1 and y == n-1:
        global answer
        answer+=1
        return
    if dirc == 'right':
        if x<n-1 and y<n-1:
            if lst[y+1][x] ==0 and lst[y][x+1]==0 and lst[y+1][x+1]==0:
                pipe(x+1,y+1,"diago")
        if x<n-1:
            if lst[y][x+1]==0:
                pipe(x+1,y,'right')
    if dirc == 'diago':
        if x<n-1:
            if lst[y][x+1]==0:
                pipe(x+1,y,'right')
        if y<n-1:
            if lst[y+1][x]==0:
                pipe(x,y+1,'down')
        if x<n-1 and y<n-1:
            if lst[y+1][x] ==0 and lst[y][x+1]==0 and lst[y+1][x+1]==0:
                pipe(x+1,y+1,"diago")       
    if dirc == 'down':
        if y<n-1:
            if lst[y+1][x]==0:
                pipe(x,y+1,'down')
        if x<n-1 and y<n-1:
            if lst[y+1][x] ==0 and lst[y][x+1]==0 and lst[y+1][x+1]==0:
                pipe(x+1,y+1,"diago")
        
    

pipe(1,0,'right')

print(answer)