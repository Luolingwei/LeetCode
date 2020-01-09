
# 思路: limit越大，k越小，找到满足curs>=K+1的最大limit, binary search
# 大于K没关系，大于K也可以等于K，因为可以两个Part合并成一个Part，limit是lower bound

class Solution:
    def maximizeSweetness(self, sweetness, K):
        def helper(limit):
            res, curs = 0, 0
            for n in sweetness:
                curs += n
                if curs >= limit:
                    res += 1
                    curs = 0
            return res

        l, r = min(sweetness), sum(sweetness)
        while l < r:
            mid = (l + r + 1) // 2
            if helper(mid) < K + 1:
                r = mid - 1
            else:
                l = mid
        return l

a=Solution()
print(a.maximizeSweetness([1,2,3,4,5,6,7,8,9],5))