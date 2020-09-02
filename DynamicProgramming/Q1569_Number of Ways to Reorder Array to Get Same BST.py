from math import factorial

# 思路: 对于一个BST, 根节点确定时，可以将节点分为两部分, recursive计算左右子树组合的方法数
# 总方法数 = C(nN) * 左子树方法数 * 右子树方法数, 因为子树的数只需要保持他们的相对位置在总数组中不变即可
# 用数组cache阶乘

class Solution:

    def __init__(self):
        self.mod = 10 ** 9 + 7
        self.fac = [1] + [0]*1000
        for i in range(1,1001):
            self.fac[i] = self.fac[i-1]*i

    def helper(self, a, b):
        return factorial(a + b) // (factorial(a) * factorial(b))

    def cal(self, nums):
        if len(nums) <= 1: return 1
        l, r = [], []
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                l.append(nums[i])
            else:
                r.append(nums[i])
        return self.cal(l) * self.cal(r) * self.fac[len(l)+len(r)]//(self.fac[len(l)]* self.fac[len(r)]) % self.mod

    def numOfWays(self, nums):
        return self.cal(nums) - 1


a=Solution()
print(a.numOfWays([2,1,3]))
print(a.numOfWays([3,1,2,5,4,6]))
print(a.numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))

