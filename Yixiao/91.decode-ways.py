#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        #191/269 cases passed (N/A)


        dp = [0 for i in range(0,len(s))]

        dp[0]=1
        if(s[0]=='0'):
            return 0
        elif(len(s)==1):
            return 1
        elif(s[0]=='1'):
            if(s[1]=='0'):
                dp[1]=1
            else:
                dp[1]=2
        elif(s[0]=='2'):
            if(int(s[1])<=6):
                dp[1]=2
            else:
                dp[1]=1
        else:
            dp[1]=1
        


        for i in range(2,len(s)):
            if(int(s[i-1:i+1])>26):
                dp[i]=dp[i-1]
            elif(s[i]=='0'):
                dp[i]=dp[i-2]
            elif(s[i-1]=='0'):
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]+1

        return dp[-1]

        
# @lc code=end

