# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

# 思路1: dp[i]表示以i结尾的Turbulent数组的最长长度.
# 思路2: dp,用up和down表示以当前位置结尾的向上和向下的最长数组长度，不断更新ans

class Solution:

    # Solution 1: classic dp
    # def maxTurbulenceSize(self, A):
    #     if len(A)==1: return 1
    #     dp=[1]*len(A)
    #     dp[1]=1+bool(A[1]!=A[0])
    #     for i in range(2,len(A)):
    #         if (A[i]-A[i-1])*(A[i-1]-A[i-2])<0: dp[i]=dp[i-1]+1
    #         else: dp[i]=1+bool(A[i]!=A[i-1])
    #     return max(dp)

    # Solution 2: dp, up and down
    def maxTurbulenceSize(self, A):
        ans=up=down=1
        for i in range(1,len(A)):
            if A[i]-A[i-1]>0:
                up,down=down+1,1
                ans=max(up,ans)
            elif A[i]-A[i-1]<0:
                down,up=up+1,1
                ans=max(down,ans)
            else:
                down=up=1
        return ans

a=Solution()
print(a.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(a.maxTurbulenceSize([4,4,4,4,4]))
print(a.maxTurbulenceSize([4,5]))
print(a.maxTurbulenceSize([4]))