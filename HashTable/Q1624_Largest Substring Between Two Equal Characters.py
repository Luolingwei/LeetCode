
# 思路: dict记录已经出现过的字母的第一个位置, 每次遇到重复字母, 更新最长长度

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        memo, res = {}, -1
        for i,c in enumerate(s):
            if c not in memo:
                memo[c] = i
            else:
                res = max(res, i-memo[c]-1)
        return res


a=Solution()
print(a.maxLengthBetweenEqualCharacters("aa"))
print(a.maxLengthBetweenEqualCharacters("abca"))
print(a.maxLengthBetweenEqualCharacters("cbzxy"))
print(a.maxLengthBetweenEqualCharacters("cabbac"))