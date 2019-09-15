# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# Given target = 5, return true.
# Given target = 20, return false.

# 思路: 从左下角开始，如果target大于当前值，向右移（当前col都比target小），如果target小于当前值，向上移（当前row都比target大）

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m,n=len(matrix),len(matrix[0])
        r,c=m-1,0
        while r>=0 and c<n:
            if matrix[r][c]==target: return True
            elif matrix[r][c]>target:
                r-=1
            else:
                c+=1
        return False

a=Solution()
print(a.searchMatrix([[1]],1))
print(a.searchMatrix([[-1,3]],1))
print(a.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5))