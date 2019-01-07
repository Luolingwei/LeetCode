class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse=0
        flag=1
        if x<0:
            x=abs(x)
            flag=-1
        while x:
            x,remainder=divmod(x,10)
            reverse=reverse*10+remainder
        if reverse < 2147483647:
            return flag*reverse
        else:
            return 0

a=Solution()
print(a.reverse(123))
print(a.reverse(120))
print(a.reverse(-123))
print(a.reverse(-999999999999999999999999999999999))



