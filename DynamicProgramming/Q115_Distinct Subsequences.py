class Solution:
    def numDistinct(self, s, t):
        state=[1]+[0]*len(t)
        for char_s in s:
            new_state=state[:]
            for i,char_t in enumerate(t):
                if char_s==char_t:
                    new_state[i+1]+=state[i]
            state=new_state
        return state[-1]

a=Solution()
print(a.numDistinct("babgbag","bag"))
print(a.numDistinct("rabbbit","rabbit"))