from functools import lru_cache

# 题意转化: 找m个size为k的window, 使得最大值最小
# 思路1: dfs, 当前点选或者不选两种情况, 取最大值, TLE
# 思路2: binary search, 0->maxNum 对最大值进行设置, 计算能形成了window数量, 取最小的能形成>=m个window的阈值
# O(nlog(maxN))

class Solution:
    # def minDays(self, bloomDay, m, k):
    #
    #     def helper(nums):
    #         stack, ans = [], []
    #         for i, n in enumerate(nums):
    #             while stack and nums[stack[-1]] < n:
    #                 stack.pop()
    #             stack.append(i)
    #             if stack[0] == i - k:
    #                 stack = stack[1:]
    #             if i >= k - 1:
    #                 ans.append(nums[stack[0]])
    #         return ans
    #
    #     maxmemo = helper(bloomDay)
    #
    #     @lru_cache(None)
    #     def dfs(pos, left):
    #         if len(bloomDay) - pos < left * k:
    #             return float('inf')
    #         if left == 0:
    #             return float('-inf')
    #         return min(max(maxmemo[pos], dfs(pos + k, left - 1)), dfs(pos + 1, left))
    #
    #     res = dfs(0, m)
    #     return -1 if res == float('inf') else res

    def minDays(self, bloomDay, m, k):
        def check(maxN):
            cursize = 0
            res = 0
            for n in bloomDay:
                if n <= maxN:
                    cursize += 1
                else:
                    res += cursize // k
                    cursize = 0
            return res + cursize // k

        if len(bloomDay) < m * k: return -1
        l, r = 0, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if check(mid) < m:
                l = mid + 1
            else:
                r = mid
        return l

a=Solution()
print(a.minDays([1,10,3,10,2],3,1))
print(a.minDays([7,7,7,7,12,7,7],2,3))
