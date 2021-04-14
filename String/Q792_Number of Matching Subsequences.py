# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

# 思路1: 对于每个w, 和s进行check是否是subsequence, O(N*LengthS), 由于本题S很长, time-consuming
# 思路2: 用iter, 仍然需要每次check S
# 思路3: 以S出发对各个word进行check, 每次匹配开头的一个字母的wordList, 直到wordList中的word所有字符被匹配(剩余长度变为0)

from collections import Counter, defaultdict

class Solution:
    def numMatchingSubseq1(self, s, words):
        def check(w, s):
            i, j, m, n = 0, 0, len(w), len(s)
            while i < m and j < n:
                while j < n and s[j] != w[i]:
                    j += 1
                if j < n:
                    i += 1
                    j += 1
            return i == m

        count, res = Counter(words), 0

        for w in count.keys():
            if check(w, s):
                res += count[w]
        return res

    def numMatchingSubseq2(self, s, words):
        count = Counter(words)
        res = 0
        for w in count.keys():
            it_S = iter(s)
            if all(c in it_S for c in w):
                res += count[w]
        return res

    def numMatchingSubseq3(self, s, words):
        to_match, res = defaultdict(list), 0

        for w in words:
            to_match[w[0]].append(w)

        for c in s:
            if c in to_match:
                cur_match = to_match.pop(c)
                for w in cur_match:
                    if len(w) == 1:
                        res += 1
                    else:
                        to_match[w[1]].append(w[1:])
        return res


a=Solution()
print(a.numMatchingSubseq1("abcde",["a", "bb", "acd", "ace"]))
print(a.numMatchingSubseq1("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

print(a.numMatchingSubseq2("abcde",["a", "bb", "acd", "ace"]))
print(a.numMatchingSubseq2("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))

print(a.numMatchingSubseq3("abcde",["a", "bb", "acd", "ace"]))
print(a.numMatchingSubseq3("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))