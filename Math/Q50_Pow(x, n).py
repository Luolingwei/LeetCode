# Input: 2.00000, 10
# Output: 1024.00000

# 思路: divide and conquer,

class Solution:

    # Solution 1 iterative
    # def myPow(self, x, n):
    #     sign=1 if n<0 else 0
    #     ans,index,n=1,0,abs(n)
    #     while index<n:
    #         temp,carry=x,1
    #         while n-index>=carry:
    #             ans = ans * temp
    #             index += carry
    #             temp=temp*temp
    #             carry=2*carry
    #     if sign==1:
    #         return 1/ans
    #     else:
    #         return ans

    def myPow(self, x, n):
        def Pow(x,n):
            if n==0:
                return 1
            temp=Pow(x,n//2)
            if n%2==0:
                return temp*temp
            else:
                return x*temp*temp
        return Pow(x,n) if n>=0 else 1/Pow(x,-n)

a=Solution()
print(a.myPow(2,-2))