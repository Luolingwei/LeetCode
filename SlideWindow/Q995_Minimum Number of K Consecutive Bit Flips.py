
# 思路1: 从左边往右考虑，头上的0一定要被flip为1, 一直到N-K, 如果还有0则不能翻转
# O(nk)

# 思路2: 从左往右考虑, 不用每次都翻转右边的k个, 记录翻转的次数奇偶即可
# 翻转条件, A[i]==1 flip==1 / A[i]==0 flip==0
# 每往前走一格, 如果翻转那么当前位的翻转次数会加1
# 同时由于向右的移动, 之前加上的翻转可能失效(超出window size K的范围)
# 将翻转过的位置进行标记, 并动态计算flip与否即可
# O(n)

class Solution:
    # def minKBitFlips(self, A, K):
    #     N,res = len(A),0
    #     for i in range(N):
    #         if A[i]==0:
    #             if i>N-K: return -1
    #             for j in range(i,i+K):
    #                 A[j]=1-A[j]
    #             res+=1
    #     return res

    def minKBitFlips(self, A, K):
        N, res = len(A), 0
        flip = 0
        for i in range(N):
            if i >= K and A[i - K] == 2:
                flip ^= 1 # 失去前面的翻转
            if A[i] == flip: # 当前位需要翻转
                if i > N - K: return -1
                flip ^= 1 # 获得当前翻转
                A[i] = 2 # 标记翻转
                res += 1
        return res


a=Solution()
print(a.minKBitFlips([0,1,0],1))
print(a.minKBitFlips([1,1,0],2))
print(a.minKBitFlips([0,0,0,1,0,1,1,0],3))