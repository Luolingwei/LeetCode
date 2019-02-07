class Solution:
    def addDigits(self, num):
        return (num-1)%9+1 if num>0 else 0

a=Solution()
print(a.addDigits(38))