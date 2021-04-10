
# 思路: 对sentence加" "处理, 代表空格, 每次index向右移动cols-1格, idx代表当前要处理的起始位置
# case 1: " "在当前行尾部, 说明前面正好装下, 此处为空格, idx+1
# case 2: 字符在当前行尾部, 但后面一个为" ", 说明到末尾正好装下, 此处为最后一个字符, idx+2, 下一行从下一个字符开始
# case 3: 字符在当前行尾部, 下一个也是字符, 说明当前word没有装下, idx回退到当前word的起始位置, 到下一行处理

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        sentence = " ".join(sentence) + " "
        idx, N = 0, len(sentence)
        for i in range(rows):
            idx += cols-1
            if sentence[idx%N] == " ":
                idx+=1
            elif sentence[(idx+1)%N] == " ":
                idx+=2
            else:
                while idx>0 and sentence[(idx-1)%N]!=" ":
                    idx-=1
        return idx//N


a=Solution()
print(a.wordsTyping(["hello", "world"], 2, 8))
print(a.wordsTyping(["a", "bcd", "e"], 3, 6))
print(a.wordsTyping(["I", "had", "apple", "pie"], 4, 5))
print(a.wordsTyping(["a"], 10000, 10000))