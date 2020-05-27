
# 思路1: 递归解决
# 考虑首部抽取0-N个字母
# 0个即抽取一个字符word[0]并与dfs(word[1:])进行一一组合
# i个即, str(i)并与dfs(word[i:])进行一一组合
# True和False代表上一轮是否抽取了数字, 如果抽取了那么这一轮不能抽取数字

# 思路2: 迭代
# 每来一个字母, 将它和现有的所有ans合并, 2种情况
# 加字母到末尾, 直接添加即可
# 加数字到末尾, 如果之前结尾是数字, 在它的基础上+1, 否则新添加一个1

class Solution:

    # def generateAbbreviations(self, word):
    #     def dfs(word,flag):
    #         if not word: return [""]
    #         res = []
    #         for i in range(len(word)+1):
    #             if i==0: res+=[word[0]+s for s in dfs(word[1:],False)]
    #             elif not flag: res += [str(i)+s for s in dfs(word[i:],True)]
    #         return res
    #     return dfs(word,False)

    def generateAbbreviations(self, word):
        ans = [""]
        for c in word:
            new_ans = []
            for s in ans:
                new_ans.append(s+c)
                if s and s[-1].isdigit():
                    news = s[:-1]+str(int(s[-1])+1)
                else:
                    news = s+"1"
                new_ans.append(news)
            ans = new_ans
        return ans


a=Solution()
print(a.generateAbbreviations("wo"))
print(a.generateAbbreviations("word"))