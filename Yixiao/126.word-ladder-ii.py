#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start
class Solution(object):

    #Time Limit Exceeded
    #21/36 cases passed (N/A)

    def filter(self, currentWord, wordList):
        output = []
        for word in wordList:
            if(len(word)==len(currentWord)):
                diff = 0
                for i in range(len(word)):
                    if(word[i]!=currentWord[i]):
                        diff += 1
                    if(diff>1):
                        break
                if(diff==1):
                    output.append(word)
        return output

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if(endWord not in wordList):
            return []

        queue = []
        queue.append([beginWord])

        succuss = []
        while(len(queue)>0):
            head = queue.pop(0)
            left = []
            for word in wordList:
                if word not in head:
                    left.append(word)
            available = self.filter(head[-1],left)
            if(endWord in available):
                if(len(succuss)>0 and len(succuss[0])<len((head+[endWord]))):
                    break
                succuss.append(head+[endWord])
            for word in available:
                queue.append(head+[word])
        return succuss
        
# @lc code=end

