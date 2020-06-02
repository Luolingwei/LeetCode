
# 思路: sliding window, 用1个index往右扫描, 大于等于k时减掉左边的, 动态更新res

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        memo = {'a', 'e', 'i', 'o', 'u'}
        res, curn = 0, 0
        for i, c in enumerate(s):
            if c in memo:
                curn += 1
            if i >= k and s[i - k] in memo:
                curn -= 1
            res = max(res, curn)
        return res

a=Solution()
print(a.maxVowels("abciiidef",3))
print(a.maxVowels("tryhard",4))
