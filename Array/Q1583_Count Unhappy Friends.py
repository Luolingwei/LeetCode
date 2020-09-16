
# 找出i更喜欢的friend, check 此friend是否也更喜欢i

class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        memo = [0]*n
        for u,v in pairs:
            memo[u] = v
            memo[v] = u
        res = 0
        for i in range(n):
            pair_n = memo[i]
            for prefer_n in preferences[i]:
                if prefer_n == pair_n: break
                pair_m = memo[prefer_n]
                if preferences[prefer_n].index(i)<preferences[prefer_n].index(pair_m):
                    res += 1
                    break
        return res


a=Solution()
print(a.unhappyFriends(4,[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],[[0, 1], [2, 3]]))
print(a.unhappyFriends(2,[[1], [0]],[[1, 0]]))