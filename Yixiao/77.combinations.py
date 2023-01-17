#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):

    def dfs(self, maxdepth, nums, path, rtn):


        if(len(path)==maxdepth):
            return rtn.append(path)
        for i in range(len(nums)):
            self.dfs(maxdepth,nums[i+1:],path+[nums[i]],rtn)


    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n+1)]
        rtn = []
        self.dfs(k, nums,[],rtn)
        return rtn
        
# @lc code=end

