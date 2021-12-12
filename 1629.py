import sys

a,b,c=map(int,sys.stdin.readline().split())

def check(a,b):
    if(b==1):
        return a%c
    elif(b%2==0):
        y=check(a,b//2)
        return y*y%c
    else:
        y=check(a,(b-1)//2)
        return y*y*a%c
print(check(a,b))