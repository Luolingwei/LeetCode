class Solution:
    def sum(self,n):
        ans,index=0,1
        for i in str(n):
            ans+=int(i)*index
            index=-index
        return ans

a=Solution()
print(a.sum(54321))
print(a.sum(46))
print(a.sum(844))