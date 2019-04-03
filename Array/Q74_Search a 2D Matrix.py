class Solution:
    def binary_search(self, list, target):
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
        for i in range(len(matrix)):
            if matrix[i][-1]>=target:
                return self.binary_search(matrix[i],target)
        return False


a=Solution()
print(a.searchMatrix([[-9,-7,-7,-5,-3],[-1,0,1,3,3],[5,7,9,11,12],[13,14,15,16,18],[19,21,22,22,22]],-4))
print(a.searchMatrix([[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]],18))
print(a.searchMatrix([[1,3,5,20]],18))
print(a.searchMatrix([[]],1))
print(a.searchMatrix([],1))
print(a.searchMatrix([[1]],1))