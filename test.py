




















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

print(quickSort(nums))
