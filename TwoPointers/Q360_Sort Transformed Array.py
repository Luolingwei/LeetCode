
# 思路1: 根据与抛物线对称轴的距离决定大小，从两端向中间搜索排序

# 思路2: 直接将值都算出来, 从两端向中间根据值的大小搜索排序, a<0先添加小的, a>0先添加大的

class Solution:
    # def sortTransformedArray(self, nums, a, b, c):
    #     def func(x):
    #         return a * x * x + b * x + c
    #     if a == 0:
    #         return [func(i) for i in nums] if b > 0 else [func(i) for i in nums[::-1]]
    #     N = len(nums)
    #     center = -b / (2 * a)
    #     res = [0] * N
    #     idx = 0 if a < 0 else N - 1
    #     plus = 1 if a < 0 else -1
    #     i, j = 0, N - 1
    #     while i <= j:
    #         if center - nums[i] > nums[j] - center:
    #             res[idx] = func(nums[i])
    #             i += 1
    #         else:
    #             res[idx] = func(nums[j])
    #             j -= 1
    #         idx += plus
    #     return res

    def sortTransformedArray(self, nums, a, b, c):
        nums = [a*x*x+b*x+c for x in nums]
        N = len(nums)
        res = [0] * N
        idx,plus = (0,1) if a < 0 else (N-1,-1)
        i, j = 0, N - 1
        while i <= j:
            if (a>=0)==(nums[i]>nums[j]):
                res[idx] = nums[i]
                i += 1
            else:
                res[idx] = nums[j]
                j -= 1
            idx += plus
        return res


a=Solution()
print(a.sortTransformedArray([-4,-2,2,4],1,3,5))
print(a.sortTransformedArray([-4,-2,2,4],-1,3,5))
print(a.sortTransformedArray([-4,-2,2,4],0,3,5))