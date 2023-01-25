#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i==0):
                    if(j==0):
                        dp[i][j]=grid[0][0]
                    else:
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                elif(j==0):
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    min = dp[i-1][j]
                    if(dp[i][j-1]<min):
                        min = dp[i][j-1]
                    dp[i][j] = min + grid[i][j]
        return dp[-1][-1]              
        
# @lc code=end

