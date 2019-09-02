# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# 思路: 从左边往右走，用dic记录已经遍历过的字母，碰到重复字母时(dic[c]在left之后，说明包含在当前字符串中)，将left移动到之前字母的后一个位置，并更新dic和maxl

class Solution:
    def lengthOfLongestSubstring(self, s):
        left,maxl=0,0
        dic={}
        for i,c in enumerate(s):
            if c in dic and dic[c]>=left:
                left=dic[c]+1
            maxl=max(maxl, i-left+1)
            dic[c]=i
        return maxl

a=Solution()
print(a.lengthOfLongestSubstring("tmmzuxt"))
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring("pwwkew"))
print(a.lengthOfLongestSubstring("dvdf"))