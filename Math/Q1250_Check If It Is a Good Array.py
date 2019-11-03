
# 思路: 最大公约数为1即可

import functools
import math
class Solution:
    def isGoodArray(self, nums):
        gcd=nums[0]
        for n in nums:
            while n:
                gcd,n=n,gcd%n
            if gcd==1: return True
        return False

    # def isGoodArray(self, nums):
    #     return functools.reduce(math.gcd,nums,0)==1

a=Solution()
print(a.isGoodArray([1]))
print(a.isGoodArray([12,5,7,23]))
print(a.isGoodArray([29,6,10]))
print(a.isGoodArray([3,6]))