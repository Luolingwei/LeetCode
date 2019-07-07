# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation:
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.

# 思路: 遇到数组下降的时候必须交换前面一组数或者当前数，分别用dp记录当前swap和no_swap的最小交换次数
# 当前数对换不换都OK时，取前面swap[i-1]和no_swap[i-1]的最小值更新swap[i]和no_swap[i]
# 当前数对必须不换时，swap[i]=swap[i-1]+1（换了前面也要跟着换）,no_swap[i]=no_swap[i-1]
# 当前数对必须换时，swap[i]=no_swap[i-1]+1, no_swap[i]=swap[i-1](不换的话前面必须换)

class Solution:
    def minSwap(self, A, B):
        N=len(A)
        swap,no_swap=[0]*N,[0]*N
        swap[0],no_swap[0]=1,0
        for i in range(1,N):
            nonchangeOK,changeOK=A[i-1]<A[i] and B[i-1]<B[i],A[i-1]<B[i] and B[i-1]<A[i]
            if nonchangeOK and changeOK: #换不换都OK，取前面最小的
                temp=min(swap[i-1],no_swap[i-1])
                swap[i]=temp+1
                no_swap[i]=temp
            elif nonchangeOK: #必须不换(如果换了前面也要换)
                swap[i]=swap[i-1]+1
                no_swap[i]=no_swap[i-1]
            else: #必须要换(如果不换前面就要换)
                swap[i]=no_swap[i-1]+1
                no_swap[i]=swap[i-1]
        return min(swap[-1],no_swap[-1])

a=Solution()
print(a.minSwap([1,3,5,4],[1,2,3,7]))
print(a.minSwap([0,4,4,5,9],[0,1,6,8,10]))