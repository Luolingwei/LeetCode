class Solution:
    def addBinary(self, a, b):
        a,b=[int(i) for i in a],[int(j) for j in b]
        ans,carry='',0
        while a or b or carry:
            carry+=(a or [0]).pop()+(b or [0]).pop()
            ans=str(carry&1)+ans
            carry>>=1
        return ans


a=Solution()
print(a.addBinary("11","1"))
print(a.addBinary("1010","1011"))
print(a.addBinary("0","0"))