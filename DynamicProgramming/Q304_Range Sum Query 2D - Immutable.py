# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12

# Construct sum matrix(count from Bottom right corner)
# Have additional eage blank line to remove edge case

class NumMatrix:

    def __init__(self, matrix):
        if matrix:
            self.sum=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    self.sum[i+1][j+1]=self.sum[i][j+1]+self.sum[i+1][j]-self.sum[i][j]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix( [[3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]])
print(obj.sumRegion(1,1,2,2))
print(obj.sumRegion(1,2,2,4))

obj = NumMatrix( [[-1]])
print(obj.sumRegion(0,0,0,0))
