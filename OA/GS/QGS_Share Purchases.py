
# 类似Q76, sliding window解法，用missing和need(Counter)找到可以cover target的strs
# 然后此时可以得到的子串数为len(s)-r，移动左边界l找到真正的最小范围，在此过程中每移动一次加一个len(s)-r，累加得到此window下生成的所有子串，继续寻找下一个window

import collections
class Solution:
    def SharePurchase(self,s):
        need=collections.Counter("ABC")
        l,missing,res=0,3,0
        for r,c in enumerate(s):
            missing-=need[c]>0
            need[c]-=1
            if not missing:
                rightn=len(s)-r
                res+=rightn
                while need[s[l]]<0:
                    need[s[l]]+=1;l+=1;res+=rightn
                need[s[l]]+=1;l+=1;missing+=1
        return res

a=Solution()
print(a.SharePurchase("ABBCZBAC"))
print(a.SharePurchase("DDABAC"))