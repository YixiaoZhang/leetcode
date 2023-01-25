#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        dp = [[1000000 for j in range(len(mat[0]))] for i in range(len(mat))]


        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if(mat[i][j]==0):
                    dp[i][j]=0
                else:
                    if(i==0 and j==0):
                        continue
                    elif(i==0):
                        dp[i][j]=dp[i][j-1]+1
                    elif(j==0):
                        dp[i][j]=dp[i-1][j]+1
                    else:
                        min = dp[i][j-1]
                        if(dp[i-1][j]<dp[i][j-1]):
                            min = dp[i-1][j]
                        dp[i][j] = min+1


        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[0])-1,-1,-1):
                min = dp[i][j]

                #see bottom
                if(i<len(dp)-1):
                    if(dp[i+1][j]<min):
                        min=dp[i+1][j]+1
                #see right
                if(j<len(dp[0])-1):
                    if(dp[i][j+1]<min):
                        min=dp[i][j+1]+1
                dp[i][j] = min
        
        return dp
        
# @lc code=end

