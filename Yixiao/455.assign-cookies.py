#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):

    

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        noOfContentChildren = 0
        g.sort()
        s.sort()

        for j in range(len(s)):
            if(s[j]>=g[noOfContentChildren]):
                noOfContentChildren += 1
            if(noOfContentChildren==len(g)):
                return noOfContentChildren
                

        return noOfContentChildren
        

        
# @lc code=end

