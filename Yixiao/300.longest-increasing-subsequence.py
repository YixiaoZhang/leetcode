#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0 for i in range(len(nums))]

        dp[0]=1
        for i in range(1,len(nums)):
            maxNum = 1
            for j in range(0,i):
                if(nums[j]<nums[i] and dp[j]>=maxNum):
                    maxNum = dp[j]+1
            dp[i] = maxNum
            
        return max(dp)
        
# @lc code=end

