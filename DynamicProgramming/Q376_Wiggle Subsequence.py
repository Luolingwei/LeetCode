# Input: [9,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
#
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
#
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2

# / / \ / \

class Solution:

    # # Solution 1 计算gap的正负并比较
    # def wiggleMaxLength(self, nums):
    #     if len(nums)<2: return len(nums)
    #     diff=nums[1]-nums[0]
    #     count=2 if diff!=0 else 1
    #     for i in range(1,len(nums)-1):
    #         new_diff=nums[i+1]-nums[i]
    #         if new_diff==0: continue
    #         if new_diff*diff<=0:
    #             count+=1
    #             diff=new_diff
    #     return count

    # Solution 2 dp记录以向上和向下结束的数组长度
    def wiggleMaxLength(self, nums):
        if not nums: return 0
        up,down=1,1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                up=down+1
            if nums[i]-nums[i-1]<0:
                down=up+1
        return max(up,down)


a=Solution()
print(a.wiggleMaxLength([1,7,4,9,2,5]))
print(a.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(a.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
print(a.wiggleMaxLength([1,1,7,7,8,9,4]))
print(a.wiggleMaxLength([1]))
print(a.wiggleMaxLength([]))