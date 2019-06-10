
# 思路: python内置函数permutations（排列）,combinations(组合).

from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles):
        return len({s[:i] for s in permutations(tiles) for i in range(1,8)})

a=Solution()
print(a.numTilePossibilities("AAB"))