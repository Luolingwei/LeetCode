class Solution:
    # Quick sort
    # def sortArray(self, nums):
    #     def quick_sort(low,high):
    #         if low>=high: return
    #         left,right=low,high
    #         key=nums[low]
    #         while low<high:
    #             while nums[high]>=key and low<high:
    #                 high-=1
    #             while nums[low]<=key and low<high:
    #                 low+=1
    #             nums[low],nums[high]=nums[high],nums[low]
    #         nums[left],nums[low]=nums[low],nums[left]
    #         quick_sort(left,low-1)
    #         quick_sort(low+1,right)
    #     quick_sort(0,len(nums)-1)
    #     return nums

    # Merge sort
    def sortArray(self, nums):
        def merge_sort(nums):
            def merge(array1,array2):
                left=right=0
                new_array=[]
                while left<len(array1) and right<len(array2):
                    if array1[left]<array2[right]:
                        new_array.append(array1[left])
                        left+=1
                    else:
                        new_array.append(array2[right])
                        right+=1
                new_array+=array1[left:]
                new_array+=array2[right:]
                return new_array

            if len(nums)<2: return nums
            mid=len(nums)//2
            left=merge_sort(nums[:mid])
            right=merge_sort(nums[mid:])
            return merge(left,right)
        return merge_sort(nums)


a=Solution()
print(a.sortArray([5,1,1,2,0,0]))
print(a.sortArray([5,2,3,1]))
print(a.sortArray([]))