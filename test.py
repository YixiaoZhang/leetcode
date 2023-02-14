
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

dp = [0 for i in range(len(s))]

for i in range(len(s)):
    if(s[:i+1] in wordDict):
        dp[i] = 1
    for j in range(0,i):
        if(dp[j]==1):
            if(s[j+1:i+1] in wordDict):
                dp[i] = 1

if(dp[-1]==1):
    print("1")
else:
    print("0")




print(dp)