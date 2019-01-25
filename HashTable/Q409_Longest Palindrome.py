import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd=0
        Counter=collections.Counter(s)
        for key,value in Counter.items():
            if value%2==1:
                odd+=1
        return len(s)-odd+1 if odd!=0 else len(s)

a=Solution()
print(a.longestPalindrome("abccccdd"))
