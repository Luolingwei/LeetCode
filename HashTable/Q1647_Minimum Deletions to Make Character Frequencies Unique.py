
# 思路: 对每一个频率数进行统计，如果出现重复的, 一直减1, 直到memo中没有或者变成0

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        memo = set()
        res = 0
        for f in freq.values():
            while f in memo:
                f -= 1
                res += 1
            if f: memo.add(f)
        return res


a=Solution()
print(a.minDeletions("aab"))
print(a.minDeletions("aaabbbcc"))
print(a.minDeletions("ceabaacb"))
print(a.minDeletions("bbcebab"))