
# 思路: 每来一个car, 如果它的速度小于之前车的速度 / 在之前车撞掉之后才撞前面的车, pop掉之前的车, 因为当前车只会撞更前面的车
# 如果stack变空, 说明当前车不可能撞 赋值-1
# 否则计算与stack[-1]的碰撞时间


class Solution:
    def getCollisionTimes(self, cars):
        stack = []
        res = [-1]*len(cars)
        for i in range(len(cars))[::-1]:
            p, s = cars[i][0], cars[i][1]
            while stack and (s<=stack[-1][1] or (stack[-1][0] - p)/(s-stack[-1][1]) > stack[-1][2]):
                stack.pop()
            if not stack:
                stack.append((p,s,float('inf')))
                res[i] = -1
            else:
                t = (stack[-1][0] - p)/(s-stack[-1][1])
                res[i] = t
                stack.append((p,s,t))
        return res


a=Solution()
print(a.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))
print(a.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]))