class Solution:
    def findComplement(self, num):
        return int('1'*(len(bin(num))-2),2)^num