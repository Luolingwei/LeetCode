from collections import Counter

# 思路: 累加记录每个pair不同sum需要move的变化, 遍历可能的sum, 取最小move即可
# 2<=sum<=min(a,b), 需要2个move
# min(a+b)<sum<a+b, 需要1个move
# sum = a+b, 需要0个move
# a+b<sum<=max(a,b)+limit, 需要1个move
# max(a+b)+limit<a+b, 需要2个move

class Solution:
    def minMoves(self, nums, limit):
        diff = Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            diff[2] += 2
            diff[min(a, b) + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[max(a, b) + limit + 1] += 1

        res, cur_move = float('inf'), 0
        for x in range(2, 2 * limit + 1):
            cur_move += diff[x]
            res = min(res, cur_move)
        return res


a=Solution()
print(a.minMoves([1,2,4,3], 4))
print(a.minMoves([1,2,2,1], 2))
print(a.minMoves([1,2,1,2], 2))