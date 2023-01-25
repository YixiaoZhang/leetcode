#
# @lc app=leetcode id=413 lang=python
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in nums]
        dp.append(0)
        left = 0
        right = 1
        while(right<len(nums)):
            while(right+1<len(nums) and nums[right+1]-nums[right]==nums[right]-nums[right-1]):
                right+=1
            size = right-left+1
            if(size>=3):
                sum = 0
                size-=2
                while(size>0):
                    sum += size
                    size -= 1
                dp[right] = sum
            left = right
            right += 1
        
        sum=0
        for i in range(len(dp)):
            sum+=dp[i]
        return sum


        
# @lc code=end

