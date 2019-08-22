# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

# 思路: 类似merge intervals, 对混合之后的AB按首元素进行排序，然后对比新加入interval和当前tail，每次更新tail

class Solution:
    def intervalIntersection(self, A, B):
        C=sorted(A+B,key=lambda x:x[0])
        res,tail=[],-1
        for start,end in C:
            if start<=tail:
                res.append([start,min(tail,end)])
                tail=max(tail,end)
            else:
                tail=end
        return res

a=Solution()
print(a.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))
print(a.intervalIntersection([[1,3]],[[2,4]]))