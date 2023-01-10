#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(nums)-1

        while(True):
            middle = int((left+right)/2)

            if(nums[middle]==target):
                return True
            
            if(left == middle or right == middle):
                if(nums[left]==target):
                    return True
                if(nums[right]==target):
                    return True
                return False

            #left sorted
            if(nums[middle]>nums[left]):
                # in left             
                if(target>=nums[left] and target<=nums[middle]):
                    right = middle - 1
                # not in left
                else:
                    left = middle + 1
            #right sorted
            elif(nums[middle]<nums[left]):
                # in right
                if(target>=nums[middle] and target<=nums[right]):
                    left = middle + 1
                else:
                    right = middle - 1

            else:
                left +=1
        
        
# @lc code=end

