def subsets2(nums):
    ans = []
    for i in range(2 ** len(nums)):
        temp = []
        for j in range(len(nums)):
            if i & 1 << j:
                temp.append(nums[j])
        ans.append(temp)
    return ans

def subsets3(nums):
    ret = [[]]
    for v in nums:
        ret += [r+[v] for r in ret]
    return ret

if __name__ == '__main__':
    subsets3([1,2,3])