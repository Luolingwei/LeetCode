
# dp[j]表示当前行取第j个coin能得到的最大value, dp[j] = max(pre_dp[k] + cur_val - abs(dist) for k in range(n))

class Solution:
    def get_coin(self, matrix):
        m, n = len(matrix), len(matrix[0])
        old_dp = matrix[0]
        for i in range(1,m):
            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = max(old_dp[k]+matrix[i][j]-abs(k-j) for k in range(n))
            old_dp = new_dp[:]
        return max(old_dp)


a=Solution()
print(a.get_coin([[1,2,1],[3,0,0]]))
print(a.get_coin([[0,3,0],[2,0,1]]))