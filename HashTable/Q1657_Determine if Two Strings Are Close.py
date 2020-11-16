
# 思路: 对两个word进行统计, 比较字符分布是否相同即可

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and Counter(c1.values()) == Counter(c2.values())


a=Solution()
print(a.closeStrings("abc", "bca"))
print(a.closeStrings("a", "aa"))
print(a.closeStrings("cabbba", "abbccc"))
print(a.closeStrings("cabbba", "aabbss"))
print(a.closeStrings("abc", "bca"))