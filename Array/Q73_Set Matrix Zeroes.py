class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        index_row=set()
        index_col=set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    index_row.add(i)
                    index_col.add(j)

        for i in range(n):
            for j in range(m):
                if i in index_row or j in index_col:
                    matrix[i][j]=0

        return matrix

a=Solution()
print(a.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(a.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))