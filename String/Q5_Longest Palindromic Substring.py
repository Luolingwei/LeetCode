# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# 思路: expand from center，记录最长的l和r下标

class Solution:
    # expand from center
    def helper(self,l,r,s):
        while l>-1 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return l+1,r-1
    def longestPalindrome(self, s):
        l,r=0,0
        for i in range(len(s)):
            a,b=self.helper(i, i, s)
            if b-a>r-l:
                l,r=a,b
            a,b=self.helper(i,i+1,s)
            if b-a>r-l:
                l,r=a,b
        return s[l:r+1]

a=Solution()
print(a.longestPalindrome("babad"))
print(a.longestPalindrome("cbbd"))
print(a.longestPalindrome("a"))
print(a.longestPalindrome(""))