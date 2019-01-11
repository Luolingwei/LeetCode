class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        label=[1 for _ in range(n)]
        for i in range(2, int(n**0.5)+1):
            for j in range(i*i,n,i):
                label[j]=0
        total=sum(label)-2
        return total

a=Solution()
print(a.countPrimes(10))
