class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        matrix=[[1]*i for i in range(1,numRows+1)]
        for i in range(numRows):
            for j in range(len(matrix[i])):
                if j!=0 and j!=len(matrix[i])-1:
                    matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
        return matrix

a=Solution()
print(a.generate(5))