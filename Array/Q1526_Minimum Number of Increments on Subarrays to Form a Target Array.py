
# 思路: Greedy increase elements, 对于一个数字, increase current n times
# 对于下一个数如果小于等于 current increase, 那么下一个不需要操作, current increase = next n
# 对于下一个数如果大于 current increase, 那么下一个需要额外的 n - current increase

class Solution:
    def minNumberOperations(self, target):
        pass_next, res = 0, 0
        for n in target:
            if pass_next < n: res += n-pass_next
            pass_next = n
        return res


a=Solution()
print(a.minNumberOperations([1,2,3,2,1]))
print(a.minNumberOperations([3,1,1,2]))
print(a.minNumberOperations([3,1,5,4,2]))
print(a.minNumberOperations([1,1,1,1]))