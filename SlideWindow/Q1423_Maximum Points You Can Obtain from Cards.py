
# 思路1: dp, 分别提前记录preS和afterS, 将k个数分配到左右两边, 寻找最大的分配方案即可
# 思路2: sliding window, 先将两个数组拼接起来, 然后从左边k个的情况遍历到右边k个情况

class Solution:
    # dp
    def maxScore(self, cardPoints, k: int) -> int:
        N = len(cardPoints)
        preS, afterS = [0]*(N+1), [0]*(N+1)
        ans = 0
        for i in range(1,N+1):
            preS[i]=preS[i-1]+cardPoints[i-1]
        for j in range(1,N+1):
            afterS[j] = afterS[j-1]+cardPoints[N-j]
        for l in range(k+1):
            ans = max(ans,preS[l]+afterS[k-l])
        return ans

    # sliding window
    def maxScore(self, cardPoints, k: int) -> int:
        N = len(cardPoints)
        curS = sum(cardPoints[-k:])
        ans = curS
        for i in range(k):
            curS += cardPoints[i]
            curS -= cardPoints[i+N-k]
            ans = max(ans,curS)
        return ans


a=Solution()
print(a.maxScore([1,2,3,4,5,6,1],3))
print(a.maxScore([2,2,2],2))
print(a.maxScore([9,7,7,9,7,7,9],7))
print(a.maxScore([1,1000,1],1))
print(a.maxScore([1,79,80,1,1,1,200,1],3))