import sys
ch=str(input())
ch_list=list(ch)
for i in range(len(ch)):
    ch_list[i]=int(ch_list[i])
k=int(input())

num_break=sys.stdin.readline().rsplit()

for i in range(len(num_break)):
    num_break[i]=int(num_break[i])

for i in range(len(ch)):
    while True:
        num=ch_list[i]
        if num in num_break:
            num_1=
            


        

print(ch)
print(num_break)