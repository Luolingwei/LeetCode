
# 思路: dp, cur记录以当前数字结尾的所有子数组的bitwise OR的值
# 每来一个数, 更新cur, 并加入当前数
# 把所有的cur加入res
# O(30N)
# 分析: 数字最大为10^9, 即最多30位
# cur中包含的以当前数组结尾的值, 最多有30个不同的数

class Solution:
    def subarrayBitwiseORs(self, A):
        res, cur = set(), set()
        for n in A:
            cur = {n|m for m in cur}|{n}
            res |= cur
        return len(res)

a=Solution()
print(a.subarrayBitwiseORs([0]))
print(a.subarrayBitwiseORs([1,1,2]))
print(a.subarrayBitwiseORs([1,2,4]))