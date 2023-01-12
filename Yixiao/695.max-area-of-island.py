#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):

    def searchIsland(self, grid, area, searchedBlock, i, j):

        if((i,j) in searchedBlock):
            return 0, searchedBlock
        if(grid[i][j]==0):
            return 0, searchedBlock.append((i,j))

        area = 1
        searchedBlock.append((i,j))

        if(i>0):
            #search (i-1,j)
            thisArea, thisSearchBlock = self.searchIsland(grid, area, searchedBlock, i-1, j)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(i<len(grid)-1):
            #search (i+1,j)
            thisArea, thisSearchBlock = self.searchIsland(grid, area, searchedBlock, i+1, j)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(j>0):
            #search (i,j-1)
            thisArea, thisSearchBlock = self.searchIsland(grid, area, searchedBlock, i, j-1)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(j<len(grid[0])-1):
            #search (i,j+1)
            thisArea, thisSearchBlock = self.searchIsland(grid, area, searchedBlock, i, j+1)
            area += thisArea
            searchedBlock.append(thisSearchBlock)

        return area, searchedBlock



    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        searchedBlock = []
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1 and ((i,j) not in searchedBlock)):
                    area, searched = self.searchIsland(grid,0, searchedBlock,i,j)
                    if(area>maxArea):
                        maxArea = area
        return maxArea




        
# @lc code=end

