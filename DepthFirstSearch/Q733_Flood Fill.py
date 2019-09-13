# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

# 思路: dfs搜索四周同color的像素即可.

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        m,n=len(image),len(image[0])
        visited=set()
        def dfs(i,j,color):
            if 0<=i<m and 0<=j<n and image[i][j]==color and (i,j) not in visited:
                image[i][j]=newColor
                visited.add((i,j))
                dfs(i,j+1,color)
                dfs(i,j-1,color)
                dfs(i+1,j,color)
                dfs(i-1,j,color)
        dfs(sr,sc,image[sr][sc])
        return image

a=Solution()
print(a.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(a.floodFill([[0,0,0],[0,1,1]],1,1,1))