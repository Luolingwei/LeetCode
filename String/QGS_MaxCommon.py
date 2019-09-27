
import collections
class Solution:
    def maxCommon(self,s):
        c=collections.Counter(s)
        common,ans=0,0
        com_strs=set()
        for i in range(len(s)-1):
            if c[s[i]]>1:
                c[s[i]]-=1
                if s[i] not in com_strs:
                    common+=1
                    com_strs.add(s[i])
            elif c[s[i]]==1:
                if s[i] in com_strs:
                    common-=1
                    com_strs.remove(s[i])
                c[s[i]]-=1
            ans=max(ans,common)
        return ans

a=Solution()
print(a.maxCommon("abcdecdefg"))
print(a.maxCommon("aabbbbaa"))
print(a.maxCommon("abcdedeara"))