import bisect

# 思路: 求第k个distance, 转化为寻找满足k个小于等于pairs的dist
# 对于一个dist, 通过遍历数组binary search寻找小于等于dist的pair数量 (nlogn)
# 如果数量小于k, 那么说明目标dist一定大于此dist(l = mid +1), 否则减小dist范围(r = mid)

class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        def check(dist):
            res = 0
            for i, n in enumerate(nums):
                j = bisect.bisect_left(nums, n - dist)
                res += i - j
            return res

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            smallers = check(mid)
            if k > smallers:
                l = mid + 1
            else:
                r = mid
        return l


a=Solution()
print(a.smallestDistancePair([1,3,1],1))
print(a.smallestDistancePair([1,3,1],2))
print(a.smallestDistancePair([1,3,1],3))