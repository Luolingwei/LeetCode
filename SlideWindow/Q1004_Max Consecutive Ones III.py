# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

# 思路: sliding windows，最多包含K个0的最大window.
# 找到window后，可以不移动i, 保持window大小不变，向后寻找更大的window，因为不可能有以前面开头的更大的window(如果有在前面就已经找到了)

class Solution:
    # Solution 1 172 ms 找到以i开头的最大window.
    # def longestOnes(self, A, K):
    #     A=A+[float('-inf')]
    #     i,ans=0,float('-inf')
    #     for j,n in enumerate(A):
    #         K-=(1-n)
    #         if K<0:
    #             ans=max(ans,j-i)
    #             while K<0:
    #                 K+=(1-A[i])
    #                 i+=1
    #     return ans

    # Solution 2 120 ms
    def longestOnes(self, A, K):
        i=0
        for j,n in enumerate(A):
            K-=(1-n)
            if K<0:
                K+=(1-A[i])
                i+=1
        return j-i+1

a=Solution()
print(a.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(a.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(a.longestOnes([0,0,0,1],4))
print(a.longestOnes([1,1,1,0,0,0,1,1,1,1],0))