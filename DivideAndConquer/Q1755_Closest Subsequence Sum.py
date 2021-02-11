import bisect

# 思路: 如果要计算所有的combination的sum, 一共2^n ≈ 2^40, 超时
# 将数组分成前后两部分, 分别计算所有的combination的sum, 分别用时 2^n ≈ 2^20 ≈ 10^6
# 遍历前一半数组的所有sum, 然后在后一半的所有sum中二分查找最逼近target的sum
# O(2^(n/2) * n)

class Solution:
    def minAbsDifference(self, nums, goal):

        def dfs(curs, i, s, array):
            if i == len(array):
                s.append(curs)
                return
            dfs(curs + array[i], i + 1, s, array)
            dfs(curs, i + 1, s, array)

        s1, s2 = set(), set()
        dfs(0, 0, s1, nums[:len(nums) // 2])
        dfs(0, 0, s2, nums[len(nums) // 2:])

        s2List = sorted(s2)
        res = float('inf')
        for x in s1:
            y = goal - x
            idx = bisect.bisect_left(s2List, y)
            if idx < len(s2):
                res = min(res, s2List[idx] - y)
            if idx > 0:
                res = min(res, y - s2List[idx - 1])
        return res


a=Solution()
print(a.minAbsDifference([5,-7,3,5], 6))
print(a.minAbsDifference([7,-9,15,-2], -5))
print(a.minAbsDifference([1,2,3], -7))