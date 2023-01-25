



s = "1123"
dp = [0 for i in range(0,len(s))]

dp[0]=1
if(s[0]=='0'):
    print(0)
elif(s[0]=='1'):
    if(s[1]=='0'):
        dp[1]=1
    else:
        dp[1]=2
elif(s[0]=='2'):
    if(int(s[1])<=6):
        dp[1]=2
    else:
        dp[1]=1
else:
    dp[1]=1



for i in range(2,len(s)):
    #have to connect with s-1
    if(int(s[i-1:i+1])>26):
        dp[i]=dp[i-1]
    elif(s[i]=='0'):
        dp[i]=dp[i-2]
    elif(s[i-1]=='0'):
        dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]+1

print(dp)
