class Solution:
    def cal(self,n):
        multi,plus=1,0
        while n:
            n,reminder=divmod(n,10)
            multi*=reminder
            plus+=reminder
        return multi-plus

a=Solution()
print(a.cal(238))