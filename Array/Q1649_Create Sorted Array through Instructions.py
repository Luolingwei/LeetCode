# 思路1: 用bisect每次寻找比当前数大的和小的个数即可
# O(n^2) TLE

# 思路2: 用python的SortedList, add复杂度为O(logn)
# O(nlogn)

# 思路3: 用BIT

import bisect
from sortedcontainers import SortedList
class Solution:
    # Solution 1
    def createSortedArray1(self, instructions) -> int:
        nums = []
        total,res = 0,0
        for n in instructions:
            smaller = bisect.bisect_left(nums, n)
            larger = total - bisect.bisect_right(nums, n)
            bisect.insort(nums,n)
            res += min(smaller,larger)
            total += 1
        return res%(10**9+7)

    # Solution 2
    def createSortedArray2(self, instructions) -> int:
        nums = SortedList()
        res = 0
        for n in instructions:
            smaller = nums.bisect_left(n)
            larger = len(nums) - nums.bisect_right(n)
            nums.add(n)
            res += min(smaller,larger)
        return res%(10**9+7)


a=Solution()
print(a.createSortedArray2([1,5,6,2]))
print(a.createSortedArray2([1,2,3,6,5,4]))
print(a.createSortedArray2([1,3,3,3,2,4,2,1,2]))