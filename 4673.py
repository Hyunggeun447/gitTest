# 셀프넘버

check=[True for _ in range(10_000_001)]

for i in range(1,10_001):
    if check[i]==True:
        k=i

        while k<10_001:
            temp=k
            while k>0:
                temp+=k%10
                k=k//10
            k=temp
            check[k]=False


for i in range(1,10_001):
    if check[i] == True:
        print(i)

