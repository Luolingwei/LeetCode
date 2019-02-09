class Solution:
    def isUgly(self, num):
        if num==0: return False
        for n in [2,3,5]:
            while num%n==0:
                num=num/n
        return num==1

a=Solution()
print(a.isUgly(14))
print(a.isUgly(8))
print(a.isUgly(6))
print(a.isUgly(0))