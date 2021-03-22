
# 思路: 因为要包含中间的nums[k], 从中间开始扩展, 往两边每次扩展大的那个数, 使minN减小地尽量慢

class Solution:
    def maximumScore(self, nums, k):
        l = r = k
        res = minN = nums[k]
        while l-1>=0 or r+1<len(nums):
            leftN = nums[l-1] if l-1>=0 else float('-inf')
            rightN = nums[r+1] if r+1<len(nums) else float('-inf')
            if leftN>rightN:
                minN = min(minN, leftN)
                l-=1
            else:
                minN = min(minN, rightN)
                r+=1
            res = max(res, minN * (r-l+1))
        return res


a=Solution()
print(a.maximumScore([1,4,3,7,4,5],3))
print(a.maximumScore([5,5,4,5,4,1,1,1],0))