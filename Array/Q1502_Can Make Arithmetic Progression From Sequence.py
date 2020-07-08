
# 思路: 通过最大值和最小值的差计算gap, 判断所有数和最小值的差值是否不同而且都是gap的整数倍

class Solution:
    def canMakeArithmeticProgression(self, arr):
        minN = min(arr)
        gap = (max(arr) - minN) / (len(arr) - 1)
        if gap == 0: return True
        diffSet = set(n - minN for n in arr)
        return len(diffSet) == len(arr) and all(d % gap == 0 for d in diffSet)

a=Solution()
print(a.canMakeArithmeticProgression([3,5,1]))
print(a.canMakeArithmeticProgression([1,2,4]))