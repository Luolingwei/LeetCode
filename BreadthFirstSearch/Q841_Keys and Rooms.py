# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.

# 思路: 按bfs顺序进入房间.最后check是否遍历了所有房间.

class Solution:
    def canVisitAllRooms(self, rooms):
        bfs,visited=[0],set()
        while bfs:
            key=bfs.pop(0)
            if key not in visited:
                bfs+=rooms[key]
                visited.add(key)
        return visited==set(range(len(rooms)))

a=Solution()
print(a.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(a.canVisitAllRooms([[1],[2],[3],[]]))