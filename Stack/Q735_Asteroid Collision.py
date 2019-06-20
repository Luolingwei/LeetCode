# Input:
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation:
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

# Input:
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation:
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

# 思路: positive->right, negtive->left

class Solution:
    def asteroidCollision(self, asteroids):
        stack=[]
        for stone in asteroids:
            if stone<0:
                while stack and stack[-1]>0 and -stone>stack[-1]:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(stone)
                elif -stone==stack[-1]:
                    stack.pop()
            else:
                stack.append(stone)
        return stack

a=Solution()
print(a.asteroidCollision([5, 10, -5]))
print(a.asteroidCollision([10, 2, -5]))
print(a.asteroidCollision([8, -8]))
print(a.asteroidCollision([10, 2, -5]))
print(a.asteroidCollision([-2, -1, 1, 2]))