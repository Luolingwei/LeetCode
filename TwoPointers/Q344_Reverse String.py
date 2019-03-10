class Solution:
    # one-line solution
    # def reverseString(self, s):
    #     return s[::-1]
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i,j=i+1,j-1
        return s

a=Solution()
print(a.reverseString(["h","e","l","l","o"]))
print(a.reverseString(["H","a","n","n","a","h"]))