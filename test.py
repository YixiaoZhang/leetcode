

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if(len(nums)==0):
        return [-1,-1]

    left = 0
    right = len(nums)-1
    find = False

    while(not find):
        middle = int((left+right)/2)
        if(nums[middle]==target):
            find = True
            break
        if(left==middle or middle==right):
            print(left,middle,right)
            break
        if(nums[middle]<target):
            left = middle
        else:
            right = middle
    
    print(middle)

    if(not find):
        return [-1,-1]
    
    

    if(middle>=1):
        front = middle-1
        while(nums[front]==target):
            front -=1
            if(front==-1):
                break
    else:
        front = middle-1

    if(middle<=len(nums)-2):
        back = middle+1
        while(nums[back]==target):
            back +=1
            if(back==len(nums)):
                break
    else:
        back = middle+1
    
    return [front+1,back-1]


print(searchRange([1,4],4))