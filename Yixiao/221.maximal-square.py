#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = int(matrix[i][j])
                if(dp[i][j]==0):
                    continue
                top = 0
                if(i>=1):
                    top = dp[i-1][j]
                left = 0
                if(j>=1):
                    left = dp[i][j-1]
                if(top>=dp[i][j] and left>=dp[i][j] and top>0 and left>0):
                    extend = 0
                    if(top>left):
                        extend = left
                    else:
                        extend = top
                    while(extend>0):
                        if(int(matrix[i-extend][j-extend])==1):
                            dp[i][j]=extend+1
                            break
                        extend-=1
        max = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if(dp[i][j]**2>max):
                    max = dp[i][j]**2

        return max


        
# @lc code=end

