#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
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

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter()
        for num in nums:
            counter[num] += 1
        values = counter.values()
        sorted = self.quickSort(values)
        thereshold = sorted[k-1]
        
        topk = []

        for key in counter.keys():
            if(counter[key]>=thereshold):
                topk.append(key)

        return topk

        
# @lc code=end

