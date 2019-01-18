class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #solution1
        # if x==0:
        #     return 0
        # sum,ans,temp,temp_num=1,1,2,4
        # while sum*temp_num<=x:
        #     while sum*temp_num<=x:
        #         sum*=temp_num
        #         ans*=temp
        #         temp_num=temp_num**2
        #         temp=temp**2
        #     if sum*4>x:
        #         while (ans+1)**2<=x:
        #             ans+=1
        #         return ans
        #     temp,temp_num = 2,4
        # return ans

        #solution2
        left,right=1,x
        while True:
            mid=(left+right)//2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            elif mid**2>x:
                right=mid
            else:
                left=mid

a=Solution()
print(a.mySqrt(8972635))
print(a.mySqrt(14))
print(a.mySqrt(1))
print(a.mySqrt(26))
print(a.mySqrt(52))
print(a.mySqrt(0))
print(a.mySqrt(9))