
# 思路: 因为所有数字都是unique的, 所以用开头数字记录每个数组
# 遍历array, 碰到memo中有的数字就合并数组进来
# 最后判断是否和原始array相等

class Solution:
    def canFormArray(self, arr, pieces):
        memo = {x[0]:x for x in pieces}
        res = []
        for n in arr:
            res += memo.get(n,[])
        return res==arr


a = Solution()
print(a.canFormArray([85], [[85]]))
print(a.canFormArray([15,88], [[88],[15]]))
print(a.canFormArray([49,18,16], [[16,18,49]]))
print(a.canFormArray([91,4,64,78], [[78],[4,64],[91]]))