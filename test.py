

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def searchCity(isConnected,city,searched):
    print("searching.."+str(city))
    searched.append(city)
    for i in range(len(isConnected)):
        if(isConnected[city][i]==1 and i not in searched):
            searched = searchCity(isConnected,i,searched)
    return searched
            

def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    searched = []
    total = 0
    for i in range(len(isConnected)):
        if(i not in searched):
            total += 1
            searched = searchCity(isConnected,i,searched)
    
    return total

for i in range(len(isConnected)):
    for j in range(len(isConnected[0])):
        print(isConnected[i][j],end="")
    print("")
    
print(findCircleNum(isConnected))











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
