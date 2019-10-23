
# 思路: 维护一个window，使得window里面始终保持k distinct element，超界时更新res

import collections
class Solution:
    def find(self,S,k):
        count=collections.Counter()
        left,distinct,res=0,0,0
        for i,char in enumerate(S):
            if not count[char]:
                distinct+=1
            count[char]+=1
            if distinct>k:
                res=max(res,i-left)
                while distinct>k:
                    dropC=S[left]
                    count[dropC]-=1
                    left+=1
                    if not count[dropC]:
                        distinct-=1
        res=max(res,i-left+1)
        return res

a=Solution()
print(a.find("abydeiffioc",2))
print(a.find("aaaaaabbbbbb",2))
print(a.find("aaaaaacbbbbbbbccc",2))
print(a.find("aaaaaacbbcbbbbccc",1))