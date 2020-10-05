from collections import Counter

# 思路: 寻找比X大的个数等于X的数, 数不一定在数组内, 用Counter记录所有数字的个数
# target X的范围是0到 min(max(nums), len(nums)), 因为比X大的最多有len(nums)个, 比max大的只有0个
# 从0 到 len(nums)遍历, Counter用来记录大于等于当前数的个数

class Solution:
    def specialArray(self, nums):
        count = Counter(nums)
        total = len(nums)
        for i in range(len(nums)+1):
            if i==total: return i
            total -= count[i]
        return -1


a=Solution()
print(a.specialArray([3,5]))
print(a.specialArray([0,0]))
print(a.specialArray([0,4,3,0,4]))