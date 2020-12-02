

# 思路: 单调栈，每来一个小的数字，会替代掉已有的比它大的数字，从栈中pop所有比它大的数
# 但是需要check剩下的元素个数是否还够填满k个, 如果不够则不能继续pop

class Solution:
    def mostCompetitive(self, nums, k):
        res = []
        L = len(nums)
        for i,n in enumerate(nums):
            while res and n<res[-1] and L-i>k-len(res):
                res.pop()
            if len(res)<k: res.append(n)
        return res


a=Solution()
print(a.mostCompetitive([3,5,2,6],2))
print(a.mostCompetitive([2,4,3,3,5,4,9,6],4))
print(a.mostCompetitive([2,4,3,3,5,4,9,6,1],4))