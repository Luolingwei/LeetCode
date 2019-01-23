class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #solution1
        num=1
        while num<n:
            temp=2
            num*=temp
            while num*temp<=n:
                num*=temp
                temp=temp**2
        return num==n

        #solution2
        # while n:
        #     if n%2==0:
        #         n=n//2
        #     else:
        #         if n==1:
        #             return True
        #         return False
        # return False

a=Solution()
print(a.isPowerOfTwo(16))
print(a.isPowerOfTwo(1))
print(a.isPowerOfTwo(218))
print(a.isPowerOfTwo(0))
print(a.isPowerOfTwo(102492889043))