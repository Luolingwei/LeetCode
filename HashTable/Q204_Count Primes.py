from math import sqrt,ceil
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0,1):
            return 0
        label=[1 for _ in range(n)]
        for i in range(2, int(ceil(sqrt(n)))):
            for j in range(i*i,n,i):
                label[j]=0
        total=sum(label)-2
        return total

a=Solution()
print(a.countPrimes(20))
