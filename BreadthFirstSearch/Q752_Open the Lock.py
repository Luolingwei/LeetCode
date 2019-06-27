# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# 思路: bfs, 每次替换一个数字，用visited防止回访. 将deadends转为set提高速度.

class Solution:
    def openLock(self, deadends, target):
        if '0000' in deadends: return -1
        bfs,visited,deadends=[('0000',0)],{'0000'},set(deadends)
        while bfs:
            code,dist=bfs.pop(0)
            if code==target: return dist
            for next_code in [code[:i]+char+code[i+1:] for i in range(4) for char in (str((int(code[i])+1)%10),str((int(code[i])-1)%10))]:
                if next_code not in deadends and next_code not in visited:
                    bfs.append((next_code,dist+1))
                    visited.add(next_code)
        return -1

a=Solution()
print(a.openLock(["0201","0101","0102","1212","2002"],'0202'))
print(a.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],'8888'))
print(a.openLock(["0000"],"8888"))