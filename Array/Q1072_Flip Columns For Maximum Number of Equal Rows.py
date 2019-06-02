
# 思路: 翻转之后能构成全0或者全1的一定是完全相同或者完全相反的行.
# 如果翻转之后同为000或者同为111，那么翻转之前的行相同.
# 如果翻转之后是000和111，那么翻转之前的行相反.
# 所以只需统计和每一行相同或相反的行数，取最大值即可.

import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        dic=collections.defaultdict(int)
        for row in matrix:
            dic[tuple(row)]+=1
            flip=[1-i for i in row]
            dic[tuple(flip)]+=1
        return max(dic.values())

a=Solution()
print(a.maxEqualRowsAfterFlips([[0,1],[1,1]]))
print(a.maxEqualRowsAfterFlips([[0]]))
print(a.maxEqualRowsAfterFlips([[0,1],[1,0]]))
print(a.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))