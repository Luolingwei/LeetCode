
# 对于每个base, 搜索所有topping的可能组合情况, 找到最接近的comb

class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        self.gap = float('inf')
        self.res = None

        def dfs(target, pos):
            if abs(target) < self.gap:
                self.gap = abs(target)
                self.res = target
            if target <= 0 or pos == len(toppingCosts): return
            for n in range(3):
                dfs(target - toppingCosts[pos] * n, pos + 1)

        for base in baseCosts:
            dfs(target - base, 0)
        return target - self.res


a=Solution()
print(a.closestCost([1,7], [3,4], 10))
print(a.closestCost([2,3], [4,5,100], 18))
print(a.closestCost([3,10], [2,5], 9))
print(a.closestCost([10], [1], 1))