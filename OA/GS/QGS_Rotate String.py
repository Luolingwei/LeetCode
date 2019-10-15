
# 思路: 对s的长度取余，先计算总的right和left，对L取余，然后根据left和right的大小进行旋转

class Solution:
    def rotate(self,s,directions,amount):
        N=len(directions)
        L=len(s)
        left=right=0
        for i in range(N):
            if directions[i]:
                right+=amount[i]
                right=right%L
            else:
                left+=amount[i]
                left=left%L
        if left==right:
            return s
        elif left>right:
            left-=right
            return s[left:]+s[:left]
        else:
            right-=left
            return s[L-right:]+s[:L-right]

a=Solution()
print(a.rotate("abc",[0,1,1],[1,3,1]))