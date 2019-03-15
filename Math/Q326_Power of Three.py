class Solution:
    # solution 1
    # def isPowerOfThree(self, n):
    #     num=1
    #     while num<n:
    #         temp=3
    #         num*=temp
    #         while num*temp<=n:
    #             num*=temp
    #             temp=temp**2
    #     return num==n

    # solution 2
    def isPowerOfThree(self, n):
        if n<1:
            return False
        while n%3==0:
            temp=3
            n=n//temp
            while n%temp==0:
                n=n//temp
                temp**2
        return n==1

a=Solution()
print(a.isPowerOfThree(27))
print(a.isPowerOfThree(28))
print(a.isPowerOfThree(2893187843785))