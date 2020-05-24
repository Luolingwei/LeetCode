
# 思路1: preS记录右下角的总和, binary search寻找最大Length
# O(mn*log(min(m,n)))

# 思路2: preS记录右下角的总和, 更新preS的同时计算最大的面积
# 因为移动一次maxLength最多加1, 每次尝试当前最大长度l+1即可
# O(mn)

class Solution:
    # 思路1
    # def maxSideLength(self, mat, threshold):
    #     m, n = len(mat), len(mat[0])
    #     maxL = min(m, n)
    #     preS = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             preS[i][j] = mat[i - 1][j - 1] + (preS[i - 1][j] + preS[i][j - 1] - preS[i - 1][j - 1])
    #
    #     def check(l):
    #         for i in range(l, m + 1):
    #             for j in range(l, n + 1):
    #                 if preS[i][j] - preS[i - l][j] - preS[i][j - l] + preS[i - l][j - l] <= threshold:
    #                     return True
    #         return False
    #
    #     l, r = 0, maxL
    #     while l < r:
    #         mid = (l + r + 1) // 2
    #         if check(mid):
    #             l = mid
    #         else:
    #             r = mid - 1
    #     return l

    # 思路2
    def maxSideLength(self, mat, threshold):
        m,n = len(mat),len(mat[0])
        preS = [[0]*(n+1) for _ in range(m+1)]
        l = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                preS[i][j] = mat[i-1][j-1]+(preS[i-1][j]+preS[i][j-1]-preS[i-1][j-1])
                tryl = l+1
                if i>=tryl and j>=tryl and preS[i][j]-preS[i-tryl][j]-preS[i][j-tryl]+preS[i-tryl][j-tryl]<=threshold:
                    l = tryl
        return l

a=Solution()
print(a.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4))
print(a.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],1))