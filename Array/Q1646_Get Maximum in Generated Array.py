
# 思路: 模拟数组生成即可

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==1: return 1
        nums = [0,1]+[0]*(n-1)
        res = 0
        for i in range(2,n+1):
            if i%2==0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2+1]
            res = max(res,nums[i])
        return res


a=Solution()
print(a.getMaximumGenerated(7))
print(a.getMaximumGenerated(2))
print(a.getMaximumGenerated(3))