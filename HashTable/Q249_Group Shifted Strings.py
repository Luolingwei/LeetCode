from collections import defaultdict

# 思路1: 根据长度分组, 然后每组进行归类
# 思路2: 给每个word生成code, 所有字母的ASCII码减去第一个字母的ASCII码

class Solution:
    # def groupStrings(self, strings):
    #     def check(w1, w2):
    #         gap = (ord(w1[0]) - ord(w2[0]) + 26) % 26
    #         for i in range(1, len(w1)):
    #             if (ord(w1[i]) - ord(w2[i]) + 26) % 26 != gap:
    #                 return False
    #         return True
    #
    #     memo = defaultdict(list)
    #     for word in strings:
    #         memo[len(word)].append(word)
    #
    #     res = []
    #     for wordlist in memo.values():
    #         tempres = []
    #         for w in wordlist:
    #             flag = 0
    #             for i in range(len(tempres)):
    #                 if check(w, tempres[i][-1]):
    #                     tempres[i].append(w)
    #                     flag = 1
    #                     break
    #             if not flag: tempres.append([w])
    #         res += tempres
    #     return res

    def groupStrings(self, strings):
        group = defaultdict(list)
        for s in strings:
            code = tuple(map(lambda x: ((ord(x) - ord(s[0]) + 26) % 26), s))
            group[code].append(s)
        return group.values()

a=Solution()
print(a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))