class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=[list(element) for element in zip(*matrix[::-1])]
        return matrix

a = Solution()
print(a.rotate([[1,2,3],[4,5,6],[7,8,9]]))