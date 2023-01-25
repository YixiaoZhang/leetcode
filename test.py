



n=12
dp = [i for i in range(0,n+1)]

dp[0]=0
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    min = dp[i]
    for j in range(2,i):
        if(i-j*j>=0 and dp[i-j*j]+1<min):
            min = dp[i-j*j]+1
    dp[i] = min

print(dp)