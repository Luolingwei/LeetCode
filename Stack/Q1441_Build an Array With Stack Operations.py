
# 思路: 从1开始选, 和target进行匹配, 匹配不上的一直增加n, ["Push","Pop"]
# 匹配上的直接加["Push"], 直到将target匹配完

class Solution:
    def buildArray(self, target, n: int):
        n = 1
        idx = 0
        res = []
        while idx < len(target):
            while target[idx] != n:
                res += ["Push", "Pop"]
                n += 1
            res += ["Push"]
            idx += 1
            n += 1
        return res

a=Solution()
print(a.buildArray([1,3],3))
print(a.buildArray([1,2,3],3))
print(a.buildArray([1,2],4))
print(a.buildArray([2,3,4],4))