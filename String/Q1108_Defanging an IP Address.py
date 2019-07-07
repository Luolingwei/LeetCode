class Solution:
    def defangIPaddr(self, address):
        return address.replace('.','[.]')

a=Solution()
print(a.defangIPaddr("1.1.1.1"))
print(a.defangIPaddr("255.100.50.0"))