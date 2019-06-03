class Solution:
    def addStrings(self, num1, num2):
        A,B=[int(i) for i in num1],[int(j) for j in num2]
        ans,carry='',0
        while A or B or carry:
            carry+=(A or [0]).pop()+(B or [0]).pop()
            carry,reminder=divmod(carry,10)
            ans=str(reminder)+ans
        return ans

a=Solution()
print(a.addStrings('123','678'))
print(a.addStrings('123','978'))
print(a.addStrings('9','99'))