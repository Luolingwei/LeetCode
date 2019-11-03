
# 思路:考虑x,y和y,x有多少对，先相同类型的相互交换需要1次，剩下的(1或者0个)不同类型的交换需要2次

class Solution:
    def minimumSwap(self, s1, s2):
        N=len(s1)
        a,b=0,0
        for i in range(N):
            if s1[i]!=s2[i]:
                if s1[i]=='x':
                    a+=1
                else:
                    b+=1
        a1,a_left=divmod(a,2)
        b1,b_left=divmod(b,2)
        if a_left!=b_left:
            return -1
        return a1+b1+a_left*2