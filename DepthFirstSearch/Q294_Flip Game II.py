
# 思路: dfs搜索某个State是否可以win
# T(n) = (n-1)*T(n-2) = (n-1)*(n-3)*T(n-4) = .... = (n-1)*(n-3)*...(1) = O(n!)
# 用memo优化之后, 小于O(n!), 时间复杂度为所有可能出现的状态的数量

class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}
        def dfs(state):
            if state in memo: return memo[state]
            for i in range(len(state)-1):
                if state[i:i+2] == "++":
                    new_state = state[:i] + "--" + state[i+2:]
                    if not dfs(new_state):
                        memo[state] = True
                        return True
            memo[state] = False
            return False
        return dfs(currentState)

a=Solution()
print(a.canWin("++++++"))
print(a.canWin("+"))