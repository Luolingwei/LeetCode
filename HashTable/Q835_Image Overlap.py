from collections import Counter

# 思路: 重叠在一起的1才计数, 所以先拿出A,B中所有1的坐标
# 然后求所有A,B中1的坐标两两之间的差值, 如果x差值和y差值对应错位的pattern
# 相同的pattern聚在一起, 即可以通过一定的错位成功叠加, 取最大的数量

class Solution:
    def largestOverlap(self, A, B):
        Aones = [(i,j) for i,row in enumerate(A) for j,n in enumerate(row) if n]
        Bones = [(i,j) for i,row in enumerate(B) for j,n in enumerate(row) if n]
        count = Counter((ax-bx,ay-by) for ax,ay in Aones for bx,by in Bones)
        return max(count.values() or [0])


a=Solution()
print(a.largestOverlap(
    [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]],
    [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]))