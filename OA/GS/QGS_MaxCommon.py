
# 思路: 用HashTable记录左边和右边的字符个数，扫一遍字符串
# 如果左边<右边-1 common+=1, 如果左边=右边-1 不变, 如果左边>右边-1 common-=1

import collections
class Solution:
    def maxCommon(self,s):
        c1=collections.Counter()
        c2=collections.Counter(s)
        common,ans=0,0
        for i in range(len(s)-1):
            curchar=s[i]
            if c1[curchar]<c2[curchar]-1:
                common+=1
            elif c1[curchar]>c2[curchar]-1:
                common-=1
            ans=max(ans,common)
            c1[curchar]+=1
            c2[curchar]-=1
        return ans

a=Solution()
print(a.maxCommon("abcdecdefg"))
print(a.maxCommon("aabbbbaa"))
print(a.maxCommon("abcdedeara"))