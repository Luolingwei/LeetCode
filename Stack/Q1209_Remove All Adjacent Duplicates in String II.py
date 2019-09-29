
#思路: 用[c,number]的结构将字符数量存储在stack中，每来一个字符，判断是否与前面相等. 如果相同，前面数量加1，满k则pop，否则新加一个[c,1]

class Solution:
    def removeDuplicates(self, s, k):
        stack=[]
        for c in s:
            if stack and c==stack[-1][0]:
                if stack[-1][1]==k-1:
                    stack.pop()
                else:
                    stack[-1][1]+=1
            else:
                stack.append([c,1])
        return "".join([c*n for c,n in stack])

a=Solution()
print(a.removeDuplicates("deeedbbcccbdaa",3))