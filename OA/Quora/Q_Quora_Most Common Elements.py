import collections
class Solution:
    def common(self,A):
        c=collections.Counter(A)
        ans,maxfreq=[],0
        for i in c.keys():
            if c[i]>maxfreq:
                ans=[i]
                maxfreq=c[i]
            elif c[i]==maxfreq:
                ans.append(i)
        return ans

a=Solution()
print(a.common([2, 2, 3, 3, 5]))