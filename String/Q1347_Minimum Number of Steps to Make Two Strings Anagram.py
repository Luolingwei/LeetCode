from collections import Counter

# 思路: 找出t中多的字符的个数即可，Counter相减只保留正数

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t) - Counter(s)).values())