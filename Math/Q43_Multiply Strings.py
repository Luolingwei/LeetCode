class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=n2=0
        for char in num1:
            n1=n1*10+(ord(char)-ord('0'))
        for char in num2:
            n2=n2*10+(ord(char)-ord('0'))
        return str(n1*n2)

a=Solution()
print(a.multiply("123","456"))
print(a.multiply("2","3"))