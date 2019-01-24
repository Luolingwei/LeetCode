class Solution:
    # expand from center
    def helper(self,l,r,s):
        while l>-1 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for i in range(len(s)):
            temp=self.helper(i, i, s)
            if len(temp)>len(res):
                res=temp
            temp=self.helper(i,i+1,s)
            if len(temp)>len(res):
                res=temp
        return res

a=Solution()
print(a.longestPalindrome("babad"))
print(a.longestPalindrome("cbbd"))
