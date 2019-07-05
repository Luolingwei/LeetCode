# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# 思路1: 用dic存储当前数字的index
# 思路2: two pointers, 从左边和右边进行逼近.
# 思路3: 固定左边的数字，在右边二分查找另外一个数字.

class Solution:
    # Solution 1 dic 40 ms
    # def twoSum(self, numbers, target):
    #     dic={}
    #     for key,value in enumerate(numbers):
    #         if target-value in dic:
    #             return [dic[target-value]+1,key+1]
    #         else:
    #             dic[value] = key

    # Solution 2 two pointers 40 ms
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while i<j:
            n=numbers[i]+numbers[j]
            if n==target:
                return [i+1,j+1]
            elif n>target:
                j-=1
            else:
                i+=1

    # Solution 3 binary search 60 ms
    # def twoSum(self, numbers, target):
    #     N=len(numbers)
    #     for i in range(N):
    #         left=target-numbers[i]
    #         l,r=i+1,N-1
    #         while l<=r:
    #             mid=(l+r)//2
    #             if numbers[mid]==left:
    #                 return [i+1,mid+1]
    #             elif numbers[mid]>left:
    #                 r=mid-1
    #             else:
    #                 l=mid+1

a=Solution()
print(a.twoSum([2,7,11,15],9))
print(a.twoSum([2,3,4],6))