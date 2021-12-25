# LCS

str1 = str(input())
str2 = str(input())

lst = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

k = 0

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            lst[i][j] = lst[i-1][j-1]+1
        else:
            lst[i][j] = max(lst[i-1][j],lst[i][j-1])

print(lst[-1][-1])