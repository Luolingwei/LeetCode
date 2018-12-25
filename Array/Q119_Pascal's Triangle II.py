class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        matrix=[[1]*i for i in range(1,rowIndex+2)]
        for i in range(rowIndex+1):
            for j in range(len(matrix[i])):
                if j!=0 and j!=len(matrix[i])-1:
                    matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
        return matrix[-1]

a=Solution()
print(a.getRow(3))
