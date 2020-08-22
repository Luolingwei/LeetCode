
# 思路: Greedy, 从前往后扫描, flip不断0，1，0，1变化
# 如果flip和当前位不一样, 即0,1/1,0, 那么需要多翻转1次

class Solution:
    def minFlips(self, target):
        flip, res = 0, 0
        for b in target:
            if str(flip) != b:
                res += 1
                flip^=1
        return res

a=Solution()
print(a.minFlips("10111"))
print(a.minFlips("00000"))
print(a.minFlips("001011101"))