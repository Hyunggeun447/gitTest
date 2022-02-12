# 달팽이는 올라가고
a,b,n=map(int, input().split())

k=n-b

if k%(a-b)==0:
    answer=k//(a-b)
else:
    answer=k//(a-b)+1

print(answer)