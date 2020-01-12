
# 思路: 每次取permutation的前两个数字进行运算，和剩下的数字组成新的数组进行dfs，直到数组中只剩下1个元素

import itertools
import math
class Solution:
    def judgePoint24(self, nums):
        def dfs(nums):
            if len(nums)==1:
                return math.isclose(nums[0],24)
            for a,b,*rest in itertools.permutations(nums):
                if dfs([a+b]+rest) or dfs([a-b]+rest) or dfs([a*b]+rest) or dfs([b and a/b]+rest):
                    return True
            return False
        return dfs(nums)

a=Solution()
print(a.judgePoint24([4,1,8,7]))
print(a.judgePoint24([3,3,8,8])) #8/(3-8/3)
print(a.judgePoint24([1,2,1,2]))