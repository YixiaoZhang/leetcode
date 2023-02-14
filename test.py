


text1 = "bsbininm"
text2 = "jmjkbkjkv"

dp = [[0 for i in range(len(text2))] for i in range(len(text1))]

for i in range(0,len(text1)):
    for j in range(0,len(text2)):
        if(i==0):
            top = 0
        else:
            top = dp[i-1][j]
        if(text1[i]==text2[j]):
            dp[i][j] = top+1
            for k in range(j+1,len(text2)):
                max = top+1
                if(i>1 and dp[i-1][k]>max):
                    max = dp[i-1][k]
                dp[i][k] = max
            break
        else:
            dp[i][j] = top

print("*",end=" ")
for i in range(0,len(text2)):
    print(text2[i],end=" ")  
print("")
for i in range(0,len(text1)):
    print(text1[i],end=" ")  
    for j in range(0,len(text2)):
        print(dp[i][j],end=" ")  
    print("")


max = 0
for i in range(0,len(text1)):
    for j in range(0,len(text2)):
        if(dp[i][j]>max):
            max = dp[i][j]
print(max)




