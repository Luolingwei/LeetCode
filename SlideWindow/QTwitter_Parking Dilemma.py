
# Sliding Window, 寻找size为k的最小间距

class Solution:
    def findroof(self,pos,k):
        pos.sort()
        j=k-1
        res=float('inf')
        while j<len(pos):
            res=min(res,pos[j]-pos[j-k+1])
            j+=1
        return res+1

a=Solution()
print(a.findroof([2,10,8,17],3))

