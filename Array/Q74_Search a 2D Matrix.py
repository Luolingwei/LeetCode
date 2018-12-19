class Solution:
    def binary_search(self, list, target):
        if list==[]:
            return False
        mid=len(list)//2
        if list[mid]==target:
            return True
        elif list[mid]>target:
            return self.binary_search(list[:mid],target)
        else:
            return self.binary_search(list[mid+1:],target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[]:
            return False
        row=-1
        n=len(matrix)
        for i in range(n):
            if matrix[i]==[]:
                return False
            if matrix[i][0]>target:
                row=i-1
                break
        return self.binary_search(matrix[row],target)

a=Solution()
print(a.searchMatrix([[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]],18))