
# 思路: 因为只能去除subarray, 所以递增序列一定是从一头开始的
# 先从两边计算最长的非递增序列, 然后试图合并两个递增序列，缩小去除的长度

class Solution:
    def findLengthOfShortestSubarray(self, arr):

        L = len(arr)
        left = 0
        while left + 1 < L and arr[left] <= arr[left + 1]:
            left += 1
        if left == L - 1: return 0

        right = L - 1
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1

        res = min(L - left - 1, right)
        low, high = 0, right
        while low <= left and high <= L - 1:
            if arr[low] <= arr[high]:
                res = min(res, high - low - 1)
                low += 1
            else:
                high += 1
        return res


a=Solution()
print(a.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
print(a.findLengthOfShortestSubarray([5,4,3,2,1]))