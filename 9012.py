# 괄호


n= int(input())

for _ in range(n):
    test=str(input())
    count=0
    for i in range(len(test)):
        if test[i]=='(':
            count+=1
        else:
            count-=1
        if count<0:
            
            break
    if count==0:
        print("YES")
    else:
        print("NO")