class Solution:
    def binary_search(self,list,target):
        l,r=0,len(list)-1
        while l<=r:
            mid=(l+r)//2
            if list[mid]==target:
                return True
            elif list[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0: return False
        row,column=[],[]
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                row.append(i)
        for j in range(len(matrix[0])):
            if matrix[0][j]<=target and matrix[len(matrix)-1][j]>=target:
                column.append(j)
        for i in row:
            if column and self.binary_search(matrix[i][column[0]:column[-1]+1],target):
                return True
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
