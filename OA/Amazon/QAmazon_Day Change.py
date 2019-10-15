# Input: [0,1,1,0],1
# Output: [1, 1, 1, 1]
#
# Input: [0,1,1,0],2
# Output: [1, 0, 0, 1]

# 思路: 用异或计算每个位置的下一天状态，计算时为了前一天的记录不被抹去，用temp存储当前数并赋给pre

class Solution:
    def Change(self,nums,D):
        def cal(array):
            pre=array[0]
            for i in range(1,len(array)-1):
                temp=array[i]
                array[i]=pre^array[i+1]
                pre=temp
        new=[0]+nums+[0]
        for _ in range(D):
            cal(new)
        return new[1:len(new)-1]

a=Solution()
print(a.Change([0,1,1,0],1))
print(a.Change([0,1,1,0],2))
print(a.Change([0,1,1,0],3))