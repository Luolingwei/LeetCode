import collections
class Solution:
    def diff(self,s1,s2):
        L1,L2=len(s1),len(s2)
        if  L1!=L2: return -1
        common=0
        c1=collections.Counter(s1)
        c2=collections.Counter(s2)
        for c in set(s1+s2):
            common+=min(c1[c],c2[c])
        return L1-common

a=Solution()
print(a.diff("tea","ate"))
print(a.diff("tea","toe"))
print(a.diff("act","acts"))