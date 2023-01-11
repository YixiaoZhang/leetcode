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
        i, j, ans = 0,0,0
        g.sort()
        s.sort()
        while i< len(g) and j< len(s):
            if s[j] >=g[i]:
                ans, i = ans+1, i+1
            j +=1
        return ans
        
# @lc code=end

