# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.

# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# 思路: 以出现次数小于k的字符进行切割（一定不能出现）,计算子字符串的返回值并取max.当所有的字符出现次数都大于等于k时，返回整个字符串长度.

class Solution:
    def longestSubstring(self, s, k):
        if len(s)<k: return 0
        for char in set(s):
            if s.count(char)<k:
                return max(self.longestSubstring(strs,k) for strs in s.split(char))
        return len(s)

a=Solution()
print(a.longestSubstring('aaabb',3))
print(a.longestSubstring('ababbc',2))
print(a.longestSubstring('a',2))