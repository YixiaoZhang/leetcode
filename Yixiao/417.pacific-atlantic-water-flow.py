#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def expand(self,heights,ocean,i,j):
        ocean[i][j] = 1
        if(i>0):
            #up
            if(heights[i][j]<=heights[i-1][j] and ocean[i-1][j]!=1):
                ocean = self.expand(heights,ocean,i-1,j)
        if(i<len(heights)-1):
            #down
            if(heights[i][j]<=heights[i+1][j] and ocean[i+1][j]!=1):
                ocean = self.expand(heights,ocean,i+1,j)
        if(j>0):
            #left
            if(heights[i][j]<=heights[i][j-1] and ocean[i][j-1]!=1):
                ocean = self.expand(heights,ocean,i,j-1)
        if(j<len(heights[0])-1):
            #right
            if(heights[i][j]<=heights[i][j+1] and ocean[i][j+1]!=1):
                ocean = self.expand(heights,ocean,i,j+1)
        return ocean

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        atlantic = []
        pacific = []
        for i in range(len(heights)):
            row1 = []
            row2 = []
            for j in range(len(heights[0])):
                row1.append(0)
                row2.append(0)
            atlantic.append(row1)
            pacific.append(row2)


        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(j==len(heights[0])-1 or i==len(heights)-1):
                    atlantic = self.expand(heights,atlantic,i,j)
                if(j==0 or i==0):
                    pacific = self.expand(heights,pacific,i,j)

        output = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(atlantic[i][j]==1 and pacific[i][j]==1):
                    output.append([i,j])

        return output


        
        
        
# @lc code=end

