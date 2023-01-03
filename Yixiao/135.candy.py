#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if(len(ratings)==1):
            return 1

        candy = [1 for i in range(len(ratings))]

        for i in range(0,len(ratings)-1):
            if(ratings[i]<ratings[i+1]):
                candy[i+1] = candy[i] + 1 
        
        for j in range(len(ratings)-1,0,-1):
            if(ratings[j-1]>ratings[j] and candy[j-1]<=candy[j]):
                candy[j-1] = candy[j]+1

        return(sum(candy))


        
# @lc code=end

