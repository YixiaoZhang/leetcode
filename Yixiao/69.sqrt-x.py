#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if(x==0):
            return 0
        if(x<4):
            return 1

        min = 0
        max = x

        while(True):
            middle = int((min+max)/2)
            middleSquare = middle*middle
            middlePlus1Square = (middle+1)*(middle+1)

            if(middleSquare<=x and middlePlus1Square>x):
                return middle
            if(middleSquare>x):
                max = middle
            else:
                min = middle
        
# @lc code=end

