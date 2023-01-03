#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if(n==0):
            return
        if(m==0):
            nums1[0:n] = nums2[0:n]
            return

        index1 = m-1
        index2 = n-1

        for i in range(m+n-1,-1,-1):
            if(nums1[index1]>=nums2[index2]):
                nums1[i] = nums1[index1]
                index1 -= 1
                if(index1==-1):
                    nums1[0:index2+1] = nums2[0:index2+1]
                    break
            else:
                nums1[i] = nums2[index2]
                index2 -= 1
                if(index2==-1):
                    break


        
# @lc code=end

