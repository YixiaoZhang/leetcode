#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            if(s[:i+1] in wordDict):
                dp[i] = 1
            for j in range(0,i):
                if(dp[j]==1):
                    if(s[j+1:i+1] in wordDict):
                        dp[i] = 1

        if(dp[-1]==1):
            return True
        else:
            return False

        
# @lc code=end

