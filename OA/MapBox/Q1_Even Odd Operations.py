class Solution:
    def getMaximumScore(self,integerArray):
        N = len(integerArray)
        preS = [0] * (N + 1)
        for i in range(1, N + 1):
            preS[i] = preS[i - 1] + integerArray[i - 1]
        memo = [[float('-inf')] * N for _ in range(N)]

        def dp(start, end, curi):
            if memo[start][end] == float('-inf'):
                if start == end:
                    memo[start][end] = integerArray[start] if curi == 1 else -integerArray[start]
                elif curi == 1:
                    memo[start][end] = preS[end + 1] - preS[start] + max(dp(start + 1, end, 0), dp(start, end - 1, 0))
                else:
                    memo[start][end] = preS[start] - preS[end + 1] + max(dp(start + 1, end, 1), dp(start, end - 1, 1))
            return memo[start][end]
        return dp(0, N - 1, 1)

a=Solution()
print(a.getMaximumScore([1,2,3]))
print(a.getMaximumScore([1,2,3,4,2,6]))
