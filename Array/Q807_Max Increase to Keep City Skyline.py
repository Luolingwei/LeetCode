# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
#
# The grid after increasing the height of buildings without affecting skylines is:
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]


# 思路: 每个格点(i,j)的限制为r_limit[i],c_limit[j]，用最小值减去grid的值

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        r_limit=list(map(max,grid))
        c_limit=list(map(max,zip(*grid)))
        return sum(min(r,c) for r in r_limit for c in c_limit)-sum(map(sum,grid))

a=Solution()
print(a.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))