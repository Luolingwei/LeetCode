
# 奇数个数的字符数<=k即可
# 同时字符个数不能少于k个
# 这里用n&1进行奇偶判断比取余更快

from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)
        return sum(n&1 for n in count.values())<=k<=len(s)


a=Solution()
print(a.canConstruct("annabelle",2))
print(a.canConstruct("leetcode",3))
print(a.canConstruct("cr",7))