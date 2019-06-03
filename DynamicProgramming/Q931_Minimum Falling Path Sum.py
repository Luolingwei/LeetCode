
# 思路: A[i][j]表示以A[i][j]结尾的最小路径. A[i][j]=A[i][j]+min(A[i-1][j-1:j+2])

class Solution:
    # Solution 1 dfs TLE
    # def minFallingPathSum(self, A):
    #     self.min=float('inf')
    #     n=len(A)
    #     def dfs(path,row,cols):
    #         if row==n:
    #             self.min=min(self.min,sum(path))
    #             return
    #         for col in cols:
    #             dfs(path+[A[row][col]],row+1,{col-1 if col>0 else col,col,col+1 if col<n-1 else col})
    #     dfs([],0,{i for i in range(n)})
    #     return self.min

    # Solution 2 DP
    def minFallingPathSum(self, A):
        n=len(A[0])
        for i in range(1,len(A)):
            for j in range(n):
                A[i][j]+=min(A[i-1][max(0,j-1):min(n,j+2)])
        return min(A[-1])


a=Solution()
print(a.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(a.minFallingPathSum([[1]]))
print(a.minFallingPathSum([[1,2],[4,5]]))