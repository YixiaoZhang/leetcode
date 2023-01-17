

nums = [1,2,3]

def per(nums):
    if(len(nums)==2):
        return [nums,[nums[1],nums[0]]]
    first = nums[0]
    last = per(nums[1:])
    outlist = []
    for item in last:
        for i in range(0,len(item)+1):
            if(i==0):
                outlist.append([first]+item)
            elif(i==len(item)):
                outlist.append(item+[first])
            else:
                outlist.append(item[:i]+[first]+item[i:])
    return outlist

print(per(nums))
            
            
