import collections

# 思路: 最后达成一致的元素一定是A+B数量最多的(至少占一半)，先找出元素
# 遍历A,B，如果某个位置A,B都不是majority则失败
# 记录A,B中不是majority的个数，返回min

class Solution:
    def minDominoRotations(self, A, B):
        count=collections.Counter(A+B)
        majority=max(count.keys(),key=lambda x:count[x])
        cA,cB=0,0
        for i in range(len(A)):
            if majority not in (A[i],B[i]):
                return -1
            if A[i]!=majority:cA+=1
            if B[i]!=majority:cB+=1
        return min(cA,cB)

a=Solution()
print(a.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(a.minDominoRotations([3,5,1,2,3],[3,6,3,3,4]))