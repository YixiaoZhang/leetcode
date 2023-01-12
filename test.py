
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]


def expand(heights,ocean,i,j):
    ocean[i][j] = 1
    if(i>0):
        #up
        if(heights[i][j]<=heights[i-1][j] and ocean[i-1][j]!=1):
            ocean = expand(heights,ocean,i-1,j)
    if(i<len(heights)-1):
        #down
        if(heights[i][j]<=heights[i+1][j] and ocean[i+1][j]!=1):
            ocean = expand(heights,ocean,i+1,j)
    if(j>0):
        #left
        if(heights[i][j]<=heights[i][j-1] and ocean[i][j-1]!=1):
            ocean = expand(heights,ocean,i,j-1)
    if(j<len(heights[0])-1):
        #right
        if(heights[i][j]<=heights[i][j+1] and ocean[i][j+1]!=1):
            ocean = expand(heights,ocean,i,j+1)
    return ocean
    

for i in range(len(heights)):
    for j in range(len(heights[0])):
        print(heights[i][j],end="")
    print("")


atlantic = []
pacific = []
for i in range(len(heights)):
    row1 = []
    row2 = []
    for j in range(len(heights[0])):
        row1.append(0)
        row2.append(0)
    atlantic.append(row1)
    pacific.append(row2)


for i in range(len(heights)):
    for j in range(len(heights[0])):
        if(j==len(heights[0])-1 or i==len(heights)-1):
            atlantic = expand(heights,atlantic,i,j)
        if(j==0 or i==0):
            pacific = expand(heights,pacific,i,j)

output = []
for i in range(len(heights)):
    for j in range(len(heights[0])):
        if(atlantic[i][j]==1 and pacific[i][j]):
            output.append([i,j])

print(output)

print("1==================")
for i in range(len(atlantic)):
    for j in range(len(atlantic[0])):
        print(atlantic[i][j],end="")
    print("")

print("2==================")
for i in range(len(pacific)):
    for j in range(len(pacific[0])):
        print(pacific[i][j],end="")
    print("")
print(atlantic[1][4],pacific[1][4])






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
