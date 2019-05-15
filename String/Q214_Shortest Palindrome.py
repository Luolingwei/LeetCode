# Input: "aacecaaa"
# Output: "aaacecaaa"
#
# Input: "abcd"
# Output: "dcbabcd"

# 思路: 寻找从s开头开始的最长回文，然后尾部的非回文部分需要在头部添加相应的字符串与之对应.
# 用t=s[::-1]作为s的翻转字符串，方便check是否回文，用两个index分别从s的末尾和t的开头出发，判断是t和s否相等，寻找最长回文。

class Solution:
    def shortestPalindrome(self, s):
        if not s: return ''
        t=s[::-1]
        index_t,index_s=0,len(s)
        while index_s>0:
            if s[:index_s]==t[index_t:]:
                return s[index_s:][::-1]+s
            index_s,index_t=index_s-1,index_t+1

a=Solution()
print(a.shortestPalindrome("aacecaaa"))
print(a.shortestPalindrome("abcd"))
print(a.shortestPalindrome("abcd"))
print(a.shortestPalindrome(""))