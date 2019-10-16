import collections
class Solution:
    def organize(self,nums):
        c=collections.Counter(nums)
        nums.sort(key=lambda x:(c[x],x))
        N,k=int(len(nums)**0.5),0
        matrix=[[0]*N for _ in range(N)]
        # 左下到右上
        # for i in range(N-1,-N-2,-1):
        #     #行-列
        #     for j in range(N-1,-1,-1):
        #         if 0<=j+i<N:
        #             matrix[j+i][j]=nums[k]
        #             k+=1
        # 右下到左上
        for i in range(2*N-2,-1,-1):
            #行+列
            for j in range(N):
                if 0<=i-j<N:
                    matrix[i-j][j]=nums[k]
                    k+=1
        return matrix

a=Solution()
print(a.organize([1,1,4,4,-2,-2,3,3,3]))