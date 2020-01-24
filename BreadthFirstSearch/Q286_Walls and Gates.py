
# 思路: 从所有gates开始bfs，修改empty的值为dist，无需记录visited.

class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms and rooms[0])
        gates = []
        dist, empty = 1, 2 ** 31 - 1

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))

        while gates:
            new_gates = []
            for x, y in gates:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < m and 0 <= newy < n and rooms[newx][newy] == empty:
                        rooms[newx][newy] = dist
                        new_gates.append((newx, newy))
            gates = new_gates
            dist += 1