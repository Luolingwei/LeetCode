class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividend1,divisor1=abs(dividend),abs(divisor)
        ans,sign=0,1
        while dividend1>=divisor1:
            temp,carry=divisor1,1
            while dividend1>=temp:
                dividend1-=temp
                ans+=carry
                temp+=temp
                carry+=carry
        if dividend*divisor<0:
            sign=-1
        if sign*ans>pow(2,31)-1 or sign*ans<-pow(2,31):
            return pow(2,31)-1
        else:
            return sign*ans

a=Solution()
print(a.divide(10,3))
print(a.divide(7,-3))
print(a.divide(1,1))
print(a.divide(8982,19))
print(a.divide(-2147483648,-1))