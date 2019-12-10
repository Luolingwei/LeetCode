class Solution:
    '''
    town judge: indegree is N-1, outdegree is 0
    '''

    def findJudge(self, N, trust):
        degree = [0] * (N + 1)
        for i, j in trust:
            degree[j] += 1
            degree[i] -= 1
        for i in range(1, N + 1):
            if degree[i] == N - 1:
                return i
        return -1