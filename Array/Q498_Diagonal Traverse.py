# Input:
# [
#  [ 1, 2,  3,  4],
#  [ 5, 6,  7,  8],
#  [ 9, 10, 11, 12]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        dic=[[] for _ in range(len(matrix)+len(matrix[0])-1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i+j)%2==0:
                    dic[i+j].insert(0,matrix[i][j])
                else:
                    dic[i+j].append(matrix[i][j])
        return [i for j in range(len(dic)) for i in dic[j]]

a=Solution()
print(a.findDiagonalOrder([
 [ 1, 2,  3,  4],
 [ 5, 6,  7,  8],
 [ 9, 10, 11, 12]
]))
print(a.findDiagonalOrder([]))



