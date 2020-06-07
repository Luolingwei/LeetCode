# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# 思路1: binary search, 找到每行最左边的1的位置，取最小值
# O(mlogn)

# 思路2: 从上往下扫, 初始位置在最右边
# 如果某行为0, 进入下一行, 如果某行为1, 继续往左扫
# O(m+n)

class Solution:
    # def leftMostColumnWithOne(self, binaryMatrix):
    #     m,n = binaryMatrix.dimensions()
    #     res = n
    #     for i in range(m):
    #         l,r = 0,n-1
    #         while l<r:
    #             mid = (l+r)//2
    #             if binaryMatrix.get(i,mid)==0:
    #                 l=mid+1
    #             else:
    #                 r=mid
    #         if binaryMatrix.get(i,l)==1: res=min(res,l)
    #     return res if res!=n else -1

    def leftMostColumnWithOne(self, binaryMatrix):
        m,n = binaryMatrix.dimensions()
        res = -1
        i,j = 0,n-1
        while i<n and j>=0:
            if binaryMatrix.get(i,j)==0:
                i+=1
            else:
                res = j
                j-=1
        return res