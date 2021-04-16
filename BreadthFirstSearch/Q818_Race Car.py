from collections import deque

# 思路: bfs, 每次添加两种情况: 加速或者反转
# prune 1: 用visited记录已经访问的(pos,speed)
# prune 2: 确保下一个pos 不会超过target绝对距离 "target", 因为如果超过一定要反转, 反转之后speed变为1, 回到initial condition


class Solution:
    def racecar(self, target: int) -> int:
        # length, position, speed
        bfs = deque([(0, 0, 1)])
        visited = set()
        while bfs:
            l, pos, speed = bfs.popleft()
            if pos == target: return l
            if (pos,speed) not in visited:
                visited.add((pos,speed))
                if abs(pos+speed-target)<target:
                    bfs.append((l+1,pos+speed,2*speed))
                bfs.append((l+1,pos,-1 if speed>0 else 1))
        return -1


a=Solution()
print(a.racecar(3))
print(a.racecar(4))
print(a.racecar(5))
print(a.racecar(6))
print(a.racecar(10))
print(a.racecar(50))