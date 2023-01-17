#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    
    def search(self, board, i, j, word):
        newboard = [row[:] for row in board]
        if(len(word)==1):
            return True
        newboard[i][j] = -1
        word = word[1:]
        
        # right
        if(i>0):
            if(newboard[i-1][j]==word[0]):
                if(self.search(newboard,i-1,j,word)):
                    return True
        
        # left
        if(i<len(newboard)-1):
            if(newboard[i+1][j]==word[0]):
                if(self.search(newboard,i+1,j,word)):
                    return True

        #top
        if(j>0):
            if(newboard[i][j-1]==word[0]):
                if(self.search(newboard,i,j-1,word)):
                    return True

        #bottom
        if(j<len(newboard[0])-1):
            if(newboard[i][j+1]==word[0]):
                if(self.search(newboard,i,j+1,word)):
                    return True
                
        return False



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]):
                    newboard = [row[:] for row in board]
                    newword = word[:]
                    if(self.search(newboard,i,j,word)):
                        return True
        return False

        
# @lc code=end

