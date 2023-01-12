

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def searchIsland(grid, area, searchedBlock, i, j):

        if((i,j) in searchedBlock):
            return 0, searchedBlock
        if(grid[i][j]==0):
            return 0, searchedBlock.append((i,j))

        area = 1
        searchedBlock.append((i,j))
        print("add",i,j,", total area is",area)


        if(i>0):
            #search (i-1,j)
            thisArea, thisSearchBlock = searchIsland(grid, area, searchedBlock, i-1, j)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(i<len(grid)-1):
            #search (i+1,j)
            thisArea, thisSearchBlock = searchIsland(grid, area, searchedBlock, i+1, j)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(j>0):
            #search (i,j-1)
            thisArea, thisSearchBlock = searchIsland(grid, area, searchedBlock, i, j-1)
            area += thisArea
            searchedBlock.append(thisSearchBlock)
        if(j<len(grid[0])-1):
            #search (i,j+1)
            thisArea, thisSearchBlock = searchIsland(grid, area, searchedBlock, i, j+1)
            area += thisArea
            searchedBlock.append(thisSearchBlock)

        
        return area, searchedBlock



def maxAreaOfIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        searchedBlock = []
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1 and ((i,j) not in searchedBlock)):
                    area, searched = searchIsland(grid,0, searchedBlock,i,j)
                    print("------",i,j,area)
                    if(area>maxArea):
                        maxArea = area
        return maxArea


for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j],end="")
    print("")
    
print(maxAreaOfIsland(grid))











nums = [1,100,1,1,1,6,7,4,7,8,9,10,1,3,5,7,9]

def quickSort(nums):
    
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

    return quickSort(nums[:left])+[nums[left]]+quickSort(nums[left+1:])

# print(quickSort(nums))
