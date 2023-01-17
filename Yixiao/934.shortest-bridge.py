#
# @lc app=leetcode id=934 lang=python
#
# [934] Shortest Bridge
#

# @lc code=start
class Solution(object):

    #there is island = true
    #there is no island = false
    def check(self, grid, grid2):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j]==1):
                    if(i>0 and grid2[i-1][j]==1):
                        return False
                    if(i<len(grid)-1 and grid2[i+1][j]==1):
                        return False
                    if(j>0 and grid2[i][j-1]==1):
                        return False
                    if(j<len(grid)-1 and grid2[i][j+1]==1):
                        return False
        return True

    def bfs(self, grid1, grid2):
        if(not self.check(grid1, grid2)):
            return 0
        newgrid = [[0 for i in range(len(grid1))] for i in range(len(grid1))]
        for i in range(len(grid1)):
            for j in range(len(grid1)):
                if(grid1[i][j]==1):
                    newgrid[i][j]=1
                    if(i>0):
                        newgrid[i-1][j]=1
                    if(i<len(grid1)-1):
                        newgrid[i+1][j]=1
                    if(j>0):
                        newgrid[i][j-1]=1
                    if(j<len(grid1)-1):
                        newgrid[i][j+1]=1
        return self.bfs(newgrid, grid2)+1



    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        island1 = [[0 for i in range(len(grid))] for i in range(len(grid))]
        label = False
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j]==1):
                    island1[i][j]=1
                    label = True
                    break
            if(label):
                break

        changing = True
        while(changing):
            changing = False
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if(island1[i][j]==1):
                        if(i>0 and grid[i-1][j]==1 and island1[i-1][j]!=1):
                            island1[i-1][j]=1
                            changing = True
                        if(i<len(grid)-1 and grid[i+1][j]==1 and island1[i+1][j]!=1):
                            island1[i+1][j]=1
                            changing = True
                        if(j>0 and grid[i][j-1]==1 and island1[i][j-1]!=1):
                            island1[i][j-1]=1
                            changing = True
                        if(j<len(grid)-1 and grid[i][j+1]==1 and island1[i][j+1]!=1):
                            island1[i][j+1]=1
                            changing = True

        island2 = [row[:] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                island2[i][j] = island2[i][j]-island1[i][j] 

        return self.bfs(island1, island2)

# @lc code=end

