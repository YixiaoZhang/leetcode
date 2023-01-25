mat = [[1,1,0],[1,1,1],[0,0,0]]


dp = [[1000 for j in range(len(mat[0]))] for i in range(len(mat))]


for i in range(len(dp)):
    for j in range(len(dp[0])):
        if(mat[i][j]==0):
            dp[i][j]=0
        else:
            if(i==0 and j==0):
                continue
            elif(i==0):
                dp[i][j]=dp[i][j-1]+1
            elif(j==0):
                dp[i][j]=dp[i-1][j]+1
            else:
                min = dp[i][j-1]
                if(dp[i-1][j]<dp[i][j-1]):
                    min = dp[i-1][j]
                dp[i][j] = min+1

for i in range(0,len(dp)):
    for j in range(0,len(dp[0])):
        print(dp[i][j],end=" ")
    print("")
print("=")

for i in range(len(dp)-1,-1,-1):
    for j in range(len(dp[0])-1,-1,-1):
        min = dp[i][j]

        #see bottom
        if(i<len(dp)-1):
            if(dp[i+1][j]<min):
                min=dp[i+1][j]+1
        #see right
        if(j<len(dp[0])-1):
            if(dp[i][j+1]<min):
                min=dp[i][j+1]+1
        dp[i][j] = min
            


for i in range(0,len(dp)):
    for j in range(0,len(dp[0])):
        print(mat[i][j],end=" ")
    print("")
print("=")
for i in range(0,len(dp)):
    for j in range(0,len(dp[0])):
        print(dp[i][j],end=" ")
    print("")