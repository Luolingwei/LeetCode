class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    count[i][j]=1
                else:
                    count[i][j]=count[i-1][j]+count[i][j-1]
        return count[n-1][m-1]

a=Solution()
print(a.uniquePaths(7,3))
print(a.uniquePaths(23,12))

