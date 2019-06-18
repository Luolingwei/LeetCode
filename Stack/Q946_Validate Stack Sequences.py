# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# 思路: 模拟push和pop的过程，当出现stack尾部等于poppped头部的数时，将stack pop.

class Solution:
    def validateStackSequences(self, pushed, popped):
        stack=[]
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[0]:
                stack.pop(),popped.pop(0)
        return not popped

a=Solution()
print(a.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))
print(a.validateStackSequences([1,2,3,4,5],[4,3,5,1,2]))
print(a.validateStackSequences([8,9,2,3,7,0,5,4,6,1],[6,8,2,1,3,9,0,7,4,5]))
