class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans+=4
                    if i-1>-1:
                        ans-=grid[i-1][j]
                    if i+1<len(grid):
                        ans-=grid[i+1][j]
                    if j-1>-1:
                        ans-=grid[i][j-1]
                    if j+1<len(grid[0]):
                        ans-=grid[i][j+1]
        return ans

a=Solution()
print(a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))