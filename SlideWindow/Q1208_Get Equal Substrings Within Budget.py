
# 思路: sliding window, 用r往前走，当maxCost<0时，达到最大size，丢掉一个l，保持这个window的size继续往下搜索. maxCost再次>0时，size将扩大.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        for r,c in enumerate(s):
            maxCost-=abs(ord(s[r])-ord(t[r]))
            if maxCost<0:
                maxCost+=abs(ord(s[l])-ord(t[l]))
                l+=1
        return r-l+1

a=Solution()
print(a.equalSubstring("a","b",1))
print(a.equalSubstring("abcd","bcdf",3))
print(a.equalSubstring("abcd","cdef",3))
print(a.equalSubstring("abcd","acde",0))
print(a.equalSubstring("krpgjbjjznpzdfy","nxargkbydxmsgby",14))
print(a.equalSubstring("tyiraojpcfuttwblehv","stbtakjkampohttraky",119))