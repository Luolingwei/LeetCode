class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign=1 if n<0 else 0
        ans,index,n=1,0,abs(n)
        while index<n:
            temp,carry=x,1
            while n-index>=carry:
                ans = ans * temp
                index += carry
                temp=temp*temp
                carry=2*carry
        if sign==1:
            return 1/ans
        else:
            return ans

a=Solution()
print(a.myPow(2,-2))