
# 思路: 从'0'*n开始('0'*n是可能的密码之一)，每次加一个数字减一个数字，加的条件是新生成的s能构成新的密码，直到构成了所有的密码k^n个
# 如果curs导致1到k都不能构成新密码则返回False，此时dfs(curs)为False，backtracking
# 此题res的长度一定为k^n+(n-1)

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start,target='0'*n,k**n
        visited={start}
        chars=['0']*n
        def dfs(s):
            if len(visited)==target: return True
            pres=s[1:]
            for i in range(k):
                curs=pres+str(i)
                if curs not in visited:
                    chars.append(str(i))
                    visited.add(curs)
                    if dfs(curs): return True
                    chars.pop()
                    visited.remove(curs)
            return False
        dfs(start)
        return ''.join(chars)

a=Solution()
print(a.crackSafe(1,2))
print(a.crackSafe(2,2))
print(a.crackSafe(2,3))
print(a.crackSafe(3,2))