# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"

#思路: 先生成board，然后计算坐标之差，为了避免走出board，先走左和上

import string
class Solution:
    def alphabetBoardPath(self, target):
        board={c:divmod(ord(c)-ord('a'),5) for c in string.ascii_lowercase}
        ans,cur='',(0,0)
        for c in target:
            pos=board[c]
            x,y=pos[1]-cur[1],pos[0]-cur[0]
            if x<0: ans+='L'*(-x)
            if y<0: ans+='U'*(-y)
            if y>0: ans+='D'*y
            if x>0: ans+='R'*x
            ans+='!'
            cur=pos
        return ans

a=Solution()
print(a.alphabetBoardPath('zdz'))
print(a.alphabetBoardPath("leet"))
print(a.alphabetBoardPath("code"))
print(a.alphabetBoardPath('zb'))