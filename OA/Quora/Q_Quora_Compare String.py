import collections
class Solution:
    def compare(self,s1,s2):
        c1,c2=collections.Counter(s1),collections.Counter(s2)
        if set(c1.keys())!=set(c2.keys()): return False
        return sorted(list(c1.values()))==sorted(list(c2.values()))

a=Solution()
print(a.compare("babzccc","abbzczz"))
print(a.compare("babzcccm","bbazzczl"))