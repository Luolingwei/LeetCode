class Solution:
    def validIPAddress(self, IP):
        nums=IP.split('.')
        for n in nums:
            if not n.isdigit():
                return False
            elif len(n)>1 and n[0]=='0':
                return False
            elif int(n)<0 or int(n)>255:
                return False
        return True

a=Solution()
print(a.validIPAddress("172.16.254.1"))
print(a.validIPAddress("-172.16.254.1"))
print(a.validIPAddress("172.016.254.1"))
print(a.validIPAddress("172.016:254.1"))

