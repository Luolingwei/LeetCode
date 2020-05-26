# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# 思路: 从左边往右走，用set记录已经遍历过的字母，碰到重复字母时一直pop左边的, 直到将当前字母pop掉
# 然后加入当前字母, 得到以当前字母结尾的最长不重复substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        j, res = 0,0
        for i,c in enumerate(s):
            while c in seen:
                seen.remove(s[j])
                j+=1
            seen.add(c)
            res = max(res, i-j+1)
        return res


a=Solution()
print(a.lengthOfLongestSubstring("tmmzuxt"))
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring("pwwkew"))
print(a.lengthOfLongestSubstring("dvdf"))