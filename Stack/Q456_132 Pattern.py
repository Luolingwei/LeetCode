class Solution:
    # Solution 1: 3 pointers, TLE O(n^3)
    # def find132pattern(self, nums):
    #     for x in range(len(nums)-2):
    #         y=x+1
    #         while y<len(nums)-1:
    #             z=y+1
    #             while z<len(nums):
    #                 if nums[x]<nums[z]<nums[y]:
    #                     return True
    #                 z+=1
    #             y+=1
    #     return False

    # Solution 2: Stack, O(n)
    # 思路: 用一个stack存储比当前值大的数，从后往前遍历nums，如果遇到比当前值小的栈顶元素，则依次弹出，存储最后一个弹出的数字为比当前元素小的最大值（num3），如果在前面找到比num3小的数，则返回True
    def find132pattern(self, nums):
        num3,stack=float('-inf'),[]
        for num in nums[::-1]:
            if num<num3:
                return True
            while stack and num>stack[-1]:
                num3=stack.pop()
            stack.append(num)
        return False

a=Solution()
print(a.find132pattern([3, 1, 4, 2]))
print(a.find132pattern([-1, 3, 2, 0]))
print(a.find132pattern([1, 2, 3, 4]))