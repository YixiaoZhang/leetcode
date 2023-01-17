

grid = [[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0]]

#not connet = true
#connect = false
def check(grid, grid2):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j]==1):
                if(i>0 and grid2[i-1][j]==1):
                    return False
                if(i<len(grid)-1 and grid2[i+1][j]==1):
                    return False
                if(j>0 and grid2[i][j-1]==1):
                    return False
                if(j<len(grid)-1 and grid2[i][j+1]==1):
                    return False
    return True

def printer(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j],end=" ")
        print("")
    print("===")

def bfs(grid1, grid2):
    if(not check(grid1, grid2)):
        return 0
    newgrid = [row[:] for row in grid1]
    for i in range(len(grid1)):
        for j in range(len(grid1)):
            if(grid1[i][j]==1):
                if(i>0):
                    newgrid[i-1][j]=1
                if(i<len(grid1)-1):
                    newgrid[i+1][j]=1
                if(j>0):
                    newgrid[i][j-1]=1
                if(j<len(grid1)-1):
                    newgrid[i][j+1]=1
    return bfs(newgrid, grid2)+1



island1 = [[0 for i in range(len(grid))] for i in range(len(grid))]
label = False
for i in range(len(grid)):
    for j in range(len(grid)):
        if(grid[i][j]==1):
            island1[i][j]=1
            label = True
            break
    if(label):
        break


changing = True
while(changing):
    changing = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(island1[i][j]==1):
                if(i>0 and grid[i-1][j]==1 and island1[i-1][j]!=1):
                    island1[i-1][j]=1
                    changing = True
                if(i<len(grid)-1 and grid[i+1][j]==1 and island1[i+1][j]!=1):
                    island1[i+1][j]=1
                    changing = True
                if(j>0 and grid[i][j-1]==1 and island1[i][j-1]!=1):
                    island1[i][j-1]=1
                    changing = True
                if(j<len(grid)-1 and grid[i][j+1]==1 and island1[i][j+1]!=1):
                    island1[i][j+1]=1
                    changing = True



island2 = [row[:] for row in grid]
for i in range(len(grid)):
    for j in range(len(grid)):
        island2[i][j] = island2[i][j]-island1[i][j] 

print("grid")
printer(grid)

print("island1")
printer(island1)

print("island2")
printer(island2)

print(bfs(island1, island2))