import bisect
class Solution:
    # solution 1 bisect
    # def countSmaller(self, nums):
    #     count,sorted=[],[]
    #     for num in nums[::-1]:
    #         index=bisect.bisect_left(sorted,num)
    #         sorted.insert(index,num)
    #         count+=[index]
    #     return count[::-1]

    #solution 2 merge_sort
    def merge(self,left,right,res):
        i,j=0,0
        new_array=[]
        while i<len(left) and j<len(right):
            if left[i][1]>right[j][1]:
                new_array+=[left[i]]
                res[left[i][0]]+=len(right)-j
                i+=1
            else:
                new_array+=[right[j]]
                j+=1
        new_array+=left[i:]
        new_array+=right[j:]
        return new_array

    def merge_sort(self,nums,res):
        if len(nums)<2:
            return nums
        mid=len(nums)//2
        left=self.merge_sort(nums[:mid],res)
        right=self.merge_sort(nums[mid:],res)
        return self.merge(left,right,res)

    def countSmaller(self, nums):
        res=[0]*len(nums)
        self.merge_sort([(i,num) for i,num in enumerate(nums)],res)
        return res

a=Solution()
print(a.countSmaller([5,2,6,1]))