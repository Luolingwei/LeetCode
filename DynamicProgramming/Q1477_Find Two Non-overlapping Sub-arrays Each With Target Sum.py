
# 思路: 计算出每个位置结尾的最短sum为target的子数组
# 用premin记录当前位置之前的最短的L[i]
# 对于一个L[i], 如果选则它作为其中一个子数组, 那么最短的可能组合为 L[i] + premin[i-L[i]]
# 对于所有的i, 用所有组合更新res

class Solution:
    def minSumOfLengths(self, arr, target):
        N, curS, res = len(arr), 0, float('inf')
        memo = {0:-1}
        L = [float('inf')]*N
        premin = [0]*N
        for i,n in enumerate(arr):
            curS += n
            if curS-target in memo:
                L[i] = i-memo[curS-target]
            if i-L[i]>=0: res = min(res, L[i] + premin[i-L[i]])
            premin[i] = min(premin[i-1], L[i]) if i>0 else L[i]
            memo[curS] = i
        return res if res!=float('inf') else -1


a=Solution()
print(a.minSumOfLengths([3,2,2,4,3],3))
print(a.minSumOfLengths([7,3,4,7],7))
print(a.minSumOfLengths([4,3,2,6,2,3,4],6))
print(a.minSumOfLengths([5,5,4,4,5],3))
print(a.minSumOfLengths([3,1,1,1,5,1,2,1],3))