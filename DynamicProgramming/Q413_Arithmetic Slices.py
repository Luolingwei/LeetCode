
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
#
# 题目意思: 给你一串数字，返回这串数字中能够构成等差数列的子串的数目。

# 思路: 等差数列长度从3开始，每增加1，子串数量增加1,2,3,4,5......

class Solution:
    def numberOfArithmeticSlices(self, A):
        count,carry=0,0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                carry+=1
                count+=carry
            else:
                carry=0
        return count

a=Solution()
print(a.numberOfArithmeticSlices([1, 2, 3, 4]))
print(a.numberOfArithmeticSlices([7, 7, 7, 7]))
print(a.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
print(a.numberOfArithmeticSlices([1, 1, 2, 5, 7]))