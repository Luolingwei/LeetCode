
# 思路: 因为只考虑subsequence的最大值最小值的, 顺序已经不需要
# 先sort, 对于一个min, 找到可以满足min+max<=target的最大max, 以它为最小值的subsequence数量为2^(r-l)个
# 向右移动l, 向左移动r.

class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        l, r = 0, len(nums)-1
        res, mod = 0, 10**9+7
        while l<=r:
            if nums[l] + nums[r] <= target:
                res += pow(2,r-l,mod)
                l += 1
            else:
                r -= 1
        return res%mod


a=Solution()
print(a.numSubseq([3,5,6,7],9))
print(a.numSubseq([3,3,6,8],10))
print(a.numSubseq([2,3,3,4,6,7],12))
print(a.numSubseq([5,2,4,1,7,6,8],16))