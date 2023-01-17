

n = 4
k = 3

nums = [i for i in range(1,n+1)]

def dfs(maxdepth, nums, path, rtn):
    if(len(path)==maxdepth):
        return rtn.append(path)
    for i in range(len(nums)):
        dfs(maxdepth,nums[i+1:],path+[nums[i]],rtn)

    

rtn = []
dfs(k, nums,[],rtn)
print(rtn)

