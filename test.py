nums = [1,2,3,1]


dp = [0 for i in nums]
dp[0] = nums[0]
dp[1] = nums[1]
for i in range(2,len(nums)):
    dp[i] = max(dp[0:i-1])

print(dp)