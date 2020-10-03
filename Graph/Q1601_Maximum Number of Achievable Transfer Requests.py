
# 思路: 题目要找到最多的requests使得整个出度和入度抵消，即所有building的出度等于入度
# brute force, 遍历所有size的requests子集, 直到找到一个让所有degree都为0的requests子集

# 思路2: 用bit mask找到所有子集, 0到1<<len(request)可以代表所有位置的情况

import itertools
class Solution:
    def maximumRequests1(self, n: int, requests):
        for k in range(len(requests),0,-1):
            for comb in itertools.combinations(range(len(requests)),k):
                degree = [0]*n
                for ridx in comb:
                    degree[requests[ridx][0]]-=1
                    degree[requests[ridx][1]]+=1
                if not any(degree):
                    return k
        return 0

    def maximumRequests2(self, n: int, requests):
        res = 0
        for mask in range(1<<len(requests)):
            degree = [0]*n
            for i in range(len(requests)):
                if (1<<i)&mask:
                    degree[requests[i][0]]-=1
                    degree[requests[i][1]]+=1
            if not any(degree):
                res = max(res, bin(mask).count('1'))
        return res


a=Solution()
print(a.maximumRequests1(5,[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
print(a.maximumRequests1(3,[[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]))
print(a.maximumRequests1(3,[[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]))
print(a.maximumRequests2(5,[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
print(a.maximumRequests2(3,[[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]))
print(a.maximumRequests2(3,[[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]))