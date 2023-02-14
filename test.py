


nums = [7,7,7,7,7,7,7]

dp = [0 for i in range(len(nums))]

dp[0]=1
for i in range(1,len(nums)):
    maxNum = 1
    for j in range(0,i):
        if(nums[j]<nums[i] and dp[j]>=maxNum):
            maxNum = dp[j]+1
    dp[i] = maxNum
    
print(max(dp))
    




