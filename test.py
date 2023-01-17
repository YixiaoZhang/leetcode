

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"



def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end=" ")
        print("")
    print("---")

def search(board, i, j, word):
    newboard = [row[:] for row in board]
    if(len(word)==1):
        return True
    newboard[i][j] = -1
    word = word[1:]
    
    # right
    if(i>0):
        if(newboard[i-1][j]==word[0]):
            if(search(newboard,i-1,j,word)):
                return True
    
    # left
    if(i<len(newboard)-1):
        if(newboard[i+1][j]==word[0]):
            if(search(newboard,i+1,j,word)):
                return True

    #top
    if(j>0):
        if(newboard[i][j-1]==word[0]):
            if(search(newboard,i,j-1,word)):
                return True

    #bottom
    if(j<len(newboard[0])-1):
        if(newboard[i][j+1]==word[0]):
            if(search(newboard,i,j+1,word)):
                return True
            
    return False



for i in range(len(board)):
    for j in range(len(board[0])):
        if(board[i][j]==word[0]):
            printboard(board)
            newboard = [row[:] for row in board]
            newword = word
            if(search(newboard,i,j,newword)):
                print("True")
        
print("F")