# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation:
# We have to delete every column.

# 思路: 用unsorted记录还未排好序的行，从第一列开始check，如果有前面的字母大于后面的unsorted，那么这一列需要删除, ans+=1. 否则保留这一列，较少unsorted.


class Solution:
    def minDeletionSize(self, A):
        ans,m,n=0,len(A),len(A[0])
        unsorted=set(range(m-1))
        for j in range(n):
            if any(A[i][j]>A[i+1][j] for i in unsorted):
                ans+=1
            else:
                unsorted-={i for i in unsorted if A[i][j]<A[i+1][j]}
        return ans

a=Solution()
# print(a.minDeletionSize(["zyx","wvu","tsr"]))
print(a.minDeletionSize(["cad","bbx","aca"]))
print(a.minDeletionSize(["zyx","wvu","tsr"]))
