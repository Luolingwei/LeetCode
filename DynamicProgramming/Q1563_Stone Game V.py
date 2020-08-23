import functools

# 思路: top down dp模拟分割的过程, 每次取sum小的部分并在小的部分继续dp, 如果相等需要比较2种情况
# 底层case为只剩1个不能分割, i==j

class Solution:
    def stoneGameV(self, stoneValue):

        preSum = [0] + stoneValue[:]
        for i in range(1, len(preSum)):
            preSum[i] += preSum[i - 1]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            res = 0
            for k in range(i, j):
                ls = preSum[k + 1] - preSum[i]
                rs = preSum[j + 1] - preSum[k + 1]
                if ls <= rs:
                    res = max(res, ls + dp(i, k))
                if ls >= rs:
                    res = max(res, rs + dp(k + 1, j))
            return res

        return dp(0, len(stoneValue) - 1)


a=Solution()
print(a.stoneGameV([6,2,3,4,5,5]))
print(a.stoneGameV([7,7,7,7,7,7,7]))
print(a.stoneGameV([4]))
print(a.stoneGameV([2,1,1]))