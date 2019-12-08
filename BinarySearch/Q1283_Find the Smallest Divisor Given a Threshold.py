from math import ceil

# divisor最大是maxN，最小是1，二分查找

class Solution:
    def smallestDivisor(self, nums, threshold):
        def helper(divisor):
            return sum(ceil(n/divisor) for n in nums)
        l,r =1,max(nums)
        while l < r:
            mid = (l + r) // 2
            if helper(mid) > threshold:
                l = mid + 1
            else:
                r = mid
        return l

a=Solution()
print(a.smallestDivisor([1,2,5,9],6))
print(a.smallestDivisor([2,3,5,7,11],11))
print(a.smallestDivisor([19],5))