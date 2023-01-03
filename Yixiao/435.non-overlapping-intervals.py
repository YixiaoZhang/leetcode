#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start

from functools import cmp_to_key
class Solution(object):

    def cmp(self, a, b):
        if(a[1]<b[1]):
            return -1
        return 1

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals,key=cmp_to_key(self.cmp))

        erase=0
        currentMax = intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<currentMax):
                erase += 1
            else:
                currentMax = intervals[i][1]

        return erase
        
# @lc code=end

