class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        l,r=0,0
        def check(i,j):
            while i>=0 and j<N and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j-1
        for i in range(len(s)):
            a,b=check(i,i)
            if b-a>r-l:
                l,r=a,b
            a,b=check(i,i+1)
            if b-a>r-l:
                l,r=a,b
        return s[l:r+1]