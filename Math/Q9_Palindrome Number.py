class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse=0
        initial=x
        if x<0:
            return False
        while x:
            x,reminder=divmod(x,10)
            reverse=reverse*10+reminder
        return reverse==initial

a=Solution()
print(a.isPalindrome(121))
print(a.isPalindrome(10))