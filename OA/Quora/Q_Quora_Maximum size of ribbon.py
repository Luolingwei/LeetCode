class Solution:
    def ribbon(self,A,k):
        l,r=1,max(A)
        while l<r:
            mid=(l+r+1)//2 #+1处理死循环
            parts=sum([i//mid for i in A])
            if parts<k:
                r=mid-1
            else:
                l=mid
        return l

a=Solution()
print(a.ribbon([1, 2, 3, 4, 9],1))
print(a.ribbon([1, 2, 3, 4, 9],2))
print(a.ribbon([1, 2, 3, 4, 9],3))
print(a.ribbon([1, 2, 3, 4, 9],5))
print(a.ribbon([1, 2, 3, 4, 9],10))
print(a.ribbon([1, 2, 3, 4, 9],100))
