from functools import cmp_to_key
class Solution:
    # sort solution
    # def largestNumber(self, nums):
    #     func=lambda a,b: 1 if str(a)+str(b)<str(b)+str(a) else -1 if str(a)+str(b)>str(b)+str(a) else 0
    #     return str(int(''.join(map(str,sorted(nums,key=cmp_to_key(func))))))

    # bubble_sort solution
    # def largestNumber(self, nums):
    #     for i in range(len(nums)):
    #         flag=0
    #         for j in range(len(nums)-i-1):
    #             if str(nums[j])+str(nums[j+1])<str(nums[j+1])+str(nums[j]):
    #                 nums[j],nums[j+1]=nums[j+1],nums[j]
    #                 flag=1
    #         if flag==0: break
    #     return str(int(''.join(map(str,nums))))

    # merge_sort solution
    def merge(self,num1,num2):
        i,j=0,0
        new_num=[]
        while i<len(num1) and j<len(num2):
            if str(num1[i])+str(num2[j])<str(num2[j])+str(num1[i]):
                new_num.append(num2[j])
                j+=1
            else:
                new_num.append(num1[i])
                i+=1
        new_num+=num1[i:]
        new_num+=num2[j:]
        return new_num

    def merge_sort(self,nums):
        if len(nums)<2: return nums
        mid=len(nums)//2
        left=self.merge_sort(nums[:mid])
        right=self.merge_sort(nums[mid:])
        return self.merge(left,right)

    def largestNumber(self, nums):
        nums=self.merge_sort(nums)
        return str(int(''.join(map(str,nums))))

a=Solution()
print(a.largestNumber([3,30,34,5,9]))
print(a.largestNumber([0,0]))