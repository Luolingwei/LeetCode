# Input: text = "loonbalxballpoon"
# Output: 2
#
# Input: text = "leetcode"
# Output: 0

# 思路: 用Counter求出text中的各字符个数，然后按个数比例统计balon能组成的字符串个数，求最小值

import collections
class Solution:
    def maxNumberOfBalloons(self, text):
        c=collections.Counter("balloon")
        count=collections.Counter(text)
        return min(count[char]//c[char]for char in c)

a=Solution()
print(a.maxNumberOfBalloons("loonbalxballpoon"))
print(a.maxNumberOfBalloons("balon"))
print(a.maxNumberOfBalloons("leetcode"))