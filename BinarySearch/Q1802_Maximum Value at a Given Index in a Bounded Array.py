

# 思路: maximize中间的数, 往两边尽量迅速减少, binary search寻找能使sum<=maxSum的最大的nums[index]

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def cal(sideN, mid):
            if sideN>=mid-1:
                sideSum = (mid*(mid+1))//2 + (sideN - (mid-1))
            else:
                sideSum = (sideN+1)*(2*mid-sideN)//2
            return sideSum

        leftN, rightN = index, n-index-1
        l, r = 1, maxSum
        while l<r:
            mid = (l+r+1)//2
            curS = cal(leftN, mid) + cal(rightN, mid) - mid
            if (curS > maxSum):
                r = mid-1
            else:
                l = mid
        return l


a=Solution()
print(a.maxValue(4,2,6))
print(a.maxValue(6,1,10))