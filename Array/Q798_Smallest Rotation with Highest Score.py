
# 思路:
# 先算出每个数字的平衡位置, 即k超过这个位置就会让这个数字index<n
# k每增加1, 会多一个数字到末尾, 即point+1(末尾index>=n)
# k=0时, 既没有gain也没有lost
# 让k 从1到N-1递进, 记录gain的变化, gain+=1-lost[k-1], 取最大gain的k

class Solution:
    def bestRotation(self, A):
        N = len(A)
        lost = [0] * N
        for i in range(N):
            lost[(i - A[i] + N) % N] += 1

        res, gain, maxgain = 0, 0, 0
        for k in range(1, N):
            gain += 1 - lost[k - 1]
            if gain > maxgain:
                res, maxgain = k, gain
        return res


a=Solution()
print(a.bestRotation([2, 3, 1, 4, 0]))
print(a.bestRotation([1, 3, 0, 2, 4]))