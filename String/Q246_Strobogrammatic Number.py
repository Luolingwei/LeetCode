class Solution:
    def isStrobogrammatic(self, num):
        trans = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        res = ""
        for i in range(len(num))[::-1]:
            if num[i] not in trans: return False
            res+=trans[num[i]]
        return res==num