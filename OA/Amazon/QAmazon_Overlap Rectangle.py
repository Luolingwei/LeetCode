class Solution:
    def overlap(self,p1,p2,q1,q2):
        if p1[1]<q2[1] or q1[1]<p2[1]:
            return False
        if p1[0]>q2[0] or q1[0]>p2[0]:
            return False
        return True

a=Solution()
print(a.overlap([0,0],[2,2],[1,1],[3,3]))