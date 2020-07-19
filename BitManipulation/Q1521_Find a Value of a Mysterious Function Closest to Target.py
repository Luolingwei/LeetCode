
# 思路: 计算出以所有数字结尾的 & 总和的结果
# 因为&操作是单调递减, 每次减少一位, 所以curSet的size最大为log(maxN), 为常数
# O(nlogm)

class Solution:
    def closestToTarget(self, arr, target):
        res = float('inf')
        curSet = set()
        for a in arr:
            curSet = {a&i for i in curSet}|{a}
            for n in curSet:
                res = min(res, abs(n-target))
        return res

a=Solution()
print(a.closestToTarget([9,12,3,7,15],5))
print(a.closestToTarget([1,2,4,8,16],0))