class Solution:
    def construct(self,n):
        ans=[]
        ans.append('*'*n)
        for _ in range(n-2):
            ans.append('*'+' '*(n-2)+'*')
        ans.append('*'*n)
        return ans

a=Solution()
print(a.construct(3))
print(a.construct(4))
print(a.construct(8))