#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
 
    def quickSort(self, nums):
        if(len(nums)<2):
            return nums

        left = 0
        right = len(nums)-1

        while(left!=right):
            if(nums[right]<nums[0]):
                right -=1
            elif(nums[left]>=nums[0]):
                left +=1
            else:
                t = nums[left]
                nums[left] = nums[right]
                nums[right] = t

        t = nums[left]
        nums[left] = nums[0]
        nums[0] = t

        return self.quickSort(nums[:left])+[nums[left]]+self.quickSort(nums[left+1:])


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums)[k-1]

    
        
# @lc code=end

