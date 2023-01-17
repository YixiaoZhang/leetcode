#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)==1):
            return [nums]
            
        if(len(nums)==2):
            return [nums,[nums[1],nums[0]]]
        first = nums[0]
        last = self.permute(nums[1:])
        outlist = []
        for item in last:
            for i in range(0,len(item)+1):
                if(i==0):
                    outlist.append([first]+item)
                elif(i==len(item)):
                    outlist.append(item+[first])
                else:
                    outlist.append(item[:i]+[first]+item[i:])
        return outlist
        
# @lc code=end

