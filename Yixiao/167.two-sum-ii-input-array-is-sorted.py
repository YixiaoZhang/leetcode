#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1

        while(l!=r):
            sum = numbers[l]+numbers[r]
            if(sum==target):
                return [l+1,r+1]
            elif(sum>target):
                r -= 1
            else:
                l += 1

        
# @lc code=end

