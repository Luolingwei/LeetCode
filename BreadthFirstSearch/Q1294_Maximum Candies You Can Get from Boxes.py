
# 思路: 类似bfs每次从有的箱子中进行访问，并取出keys，boxes，candy，如果某一轮任何箱子都没打开，游戏终止

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        curboxes=initialBoxes
        curkeys=set()
        curcandy=0
        visited=set()
        while True:
            flag=0
            for box in curboxes:
                if box not in visited:
                    if status[box]==1 or box in curkeys:
                        curcandy+=candies[box]
                        curkeys|=set(keys[box])
                        curboxes+=containedBoxes[box]
                        visited.add(box)
                        flag=1
            if not flag:
                break
        return curcandy