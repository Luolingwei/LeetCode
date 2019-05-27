
# 思路: 用tail记录最后一个下跌处的末尾，这个位置就是要被替换的数，用target记录下跌处后面比tail小的最大的数，最后将tail和target位置的数互换即可。

class Solution:
    def prevPermOpt1(self, A):
        B=A+[float('inf')]
        tail,target=-1,-1
        for i in range(len(B)-1):
            if B[i]<=B[i+1]:
                if tail!=-1 and B[i]<B[tail] and B[i]!=B[i-1]:
                    target=i
            else:
                tail=i
        A[target],A[tail]=A[tail],A[target]
        return A

a=Solution()
print(a.prevPermOpt1([3,2,1]))
print(a.prevPermOpt1([1,1,5]))
print(a.prevPermOpt1([1,9,4,6,7]))
print(a.prevPermOpt1([4,3,3,1,1]))
print(a.prevPermOpt1([3,1,1,3]))
print(a.prevPermOpt1([2,1,2,1,1,2,2,1]))