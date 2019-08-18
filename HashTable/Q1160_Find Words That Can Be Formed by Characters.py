# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# 思路: 用Counter相减进行比较，如果相减之后为空则说明word被包含

from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        C=Counter(chars)
        return sum(len(word) for word in words if not Counter(word)-C)

a=Solution()
print(a.countCharacters(["cat","bt","hat","tree"],"atach"))
print(a.countCharacters(["hello","world","leetcode"],"welldonehoneyr"))