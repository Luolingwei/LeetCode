# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

# 思路: 固定一个L窗口，加上左右长为M的最大值，这里用S计算数组的累积和，方便计算。preMax记录截至第i个数的L长度最大值，afMax记录第i个数之后的L长度最大值.

class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        res,l=0,len(A)
        S,preMax,afMax=[0]*(l+1),[0]*(l+1),[0]*(l+1)
        for i in range(1,l+1):
            S[i]+=S[i-1]+A[i-1]
        for i in range(L,l+1):
            preMax[i]=max(preMax[i-1],S[i]-S[i-L])
        for i in range(l-L,-1,-1):
            afMax[i]=max(afMax[i+1],S[i+L]-S[i])
        for i in range(l-M+1):
            res=max(res,S[i+M]-S[i]+max(preMax[i],afMax[i+M]))
        return res

a=Solution()
print(a.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))