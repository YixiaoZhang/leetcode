#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(0,n+1)]

        for i in range(1,n+1):
            min = dp[i]
            for j in range(2,i):
                if(i-j*j<0):
                    break
                if(dp[i-j*j]+1<min):
                    min = dp[i-j*j]+1
            dp[i] = min
        return dp[n]


        
# @lc code=end

