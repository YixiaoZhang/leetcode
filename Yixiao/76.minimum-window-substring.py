#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #Time Limit Exceeded
        #265/267 cases passed (N/A)

        if(len(t)>len(s)):
            return ""

        start = -1
        end = -1
        length = len(s)+1
        find = False

        for i in range(0,len(s)):
            tCounter = Counter(t)
            sCounter = Counter(s[i:i+len(t)])
            tCounter = tCounter-sCounter

            if(sum(tCounter.values())==0):
                    return s[i:i+len(t)]

            j = i+len(t)
            while(j<len(s) and j-i+1<length):
                if(tCounter[s[j]]>0):
                    tCounter[s[j]] -= 1
                if(sum(tCounter.values())==0):
                    start = i
                    end = j
                    length=end-start+1
                    find = True
                    break
                j+=1

        if(not find):
            return ""

        return s[start:end+1]

        
# @lc code=end

