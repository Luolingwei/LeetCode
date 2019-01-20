class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        #solution1 递归，慢
        # if N<2:
        #     return N
        # return self.fib(N-1)+self.fib(N-2)

        #solution2 迭代，快
        num=[0]*(N+1)
        if N==0:
            return 0
        num[1],cur=1,2
        while cur<=N:
            num[cur]=num[cur-1]+num[cur-2]
            cur+=1
        return num[N]

a=Solution()
print(a.fib(4))
print(a.fib(1))
print(a.fib(2))
print(a.fib(0))