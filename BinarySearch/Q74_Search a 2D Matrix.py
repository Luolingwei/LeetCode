
# 思路1: 先用二分查找寻找target所在的row(第一个尾部比target大的row)，然后在当前row二分查找target
# 思路2: 利用坐标将matrix转化为线性数组，进行二分查找

class Solution:

    # Solution 1 76 ms
    # def binary_search(self, list, target):
    #     l,r=0,len(list)-1
    #     while l<=r:
    #         mid=(l+r)//2
    #         if list[mid]==target:
    #             return True
    #         elif list[mid]<target:
    #             l=mid+1
    #         else:
    #             r=mid-1
    #     return False
    #
    # def searchMatrix(self, matrix, target):
    #     if not matrix: return False
    #     m,n=len(matrix),len(matrix[0])
    #     r0,r1=0,m-1
    #     while r0<r1:
    #         mid=(r0+r1)//2
    #         if matrix[mid][n-1]<target:
    #             r0=mid+1
    #         else:
    #             r1=mid
    #     return self.binary_search(matrix[r0],target)

    # Solution 2 72 ms
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            v=matrix[mid//n][mid%n]
            if v==target: return True
            elif v<target: l=mid+1
            else: r=mid-1
        return False


a=Solution()
print(a.searchMatrix([[-9,-7,-7,-5,-3],[-1,0,1,3,3],[5,7,9,11,12],[13,14,15,16,18],[19,21,22,22,22]],-4))
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))
print(a.searchMatrix([[1,3,5,20]],18))
print(a.searchMatrix([[]],1))
print(a.searchMatrix([],1))
print(a.searchMatrix([[1]],1))