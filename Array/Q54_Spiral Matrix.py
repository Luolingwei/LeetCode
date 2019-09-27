
# 思路: 用moves=[(0,1),(1,0),(0,-1),(-1,0)]控制转向，当newx和newy不符合条件时(超出边界或者碰到visited)，转向
# 结束条件为转向后仍然是visited, 表明已经旋转到最内层

class Solution:
    def spiralOrder(self, matrix):
        m,n=len(matrix),len(matrix and matrix[0])
        if not m or not n: return []
        visited=[[0]*n for _ in range(m)]
        moves=[(0,1),(1,0),(0,-1),(-1,0)]
        ans,i,x,y=[],0,0,0
        while not visited[x][y]:
            ans.append(matrix[x][y])
            visited[x][y]=1
            newx,newy=x+moves[i][0],y+moves[i][1]
            if 0<=newx<m and 0<=newy<n and not visited[newx][newy]:
                x,y=newx,newy
            else:
                i=(i+1)%4
                x,y=x+moves[i][0],y+moves[i][1]
                if x<0 or x>=m or y<0 or y>=n: break
        return ans

a=Solution()
print(a.spiralOrder([]))
print(a.spiralOrder([[]]))
print(a.spiralOrder([[1,2,3]]))
print(a.spiralOrder([[1],[2],[3]]))
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(a.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]))