from collections import Counter

# 思路1: 记录k长度的substring的unique char个数, 如果等于k, 那么无重复
# 思路2: 计算以每个char结尾的最长的无重复substring, 如果长度大于等于k, 那么符合要求

class Solution:
    # def numKLenSubstrNoRepeats(self, S, K):
    #     count,res,L = Counter(),0,0
    #     for i,c in enumerate(S):
    #         if not count[c]: L+=1
    #         count[c]+=1
    #         if i>=K:
    #             count[S[i-K]]-=1
    #             if count[S[i-K]]==0:
    #                 L-=1
    #         if L==K: res+=1
    #     return res

    def numKLenSubstrNoRepeats(self, S, K):
        seen = set()
        j, res = 0,0
        for i,c in enumerate(S):
            while c in seen:
                seen.remove(S[j])
                j+=1
            seen.add(c)
            if i-j+1>=K:
                res+=1
        return res

a=Solution()
print(a.numKLenSubstrNoRepeats("havefunonleetcode",5))
print(a.numKLenSubstrNoRepeats("home",5))