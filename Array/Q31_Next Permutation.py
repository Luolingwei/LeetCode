class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 152432 153422
        # 134285 134582
        dic={}
        store=[]
        l=len(nums)
        index=l-1
        placed_index=None

        #找到替换数字
        while index>0:
            if nums[index]>nums[index-1]:
                placed_index=index-1
                break
            else:
                index=index-1

        if placed_index==None:
            nums.sort()
        else:
            #找到替换数字后面比其大的最小数字
            new_index=placed_index+1
            while new_index<l:
                if nums[new_index]>nums[placed_index]:
                    dic[nums[new_index]]=new_index
                new_index=new_index+1
            place_index=dic[min(dic.keys())]

            #进行替换
            median=nums[placed_index]
            nums[placed_index]=nums[place_index]
            nums[place_index]=median

            #对替换数字之后的数进行排序
            search_index=placed_index+1
            while search_index < l:
                store.append(nums[search_index])
                search_index=search_index+1
            store.sort()

            sort_index=placed_index+1
            i=0
            while sort_index < l:
                nums[sort_index]=store[i]
                sort_index=sort_index+1
                i=i+1

        return nums

a=Solution()
print(a.nextPermutation([1,5,2,4,3,2]))
print(a.nextPermutation([1,3,4,2,8,5]))
print(a.nextPermutation([1]))
print(a.nextPermutation([3,2,1]))











