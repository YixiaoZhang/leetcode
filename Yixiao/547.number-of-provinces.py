#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start
class Solution(object):

    def searchCity(self,isConnected,city,searched):
        searched.append(city)
        for i in range(len(isConnected)):
            if(isConnected[city][i]==1 and i not in searched):
                searched = self.searchCity(isConnected,i,searched)
        return searched
                

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        searched = []
        total = 0
        for i in range(len(isConnected)):
            if(i not in searched):
                total += 1
                searched = self.searchCity(isConnected,i,searched)
        
        return total
                
            

        
# @lc code=end

