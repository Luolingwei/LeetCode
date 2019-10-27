import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        strs=paragraph.split()
        ban=set(banned)
        count=collections.Counter(w for w in strs if w not in ban)
        ans,freq=[],0
        for char in count:
            if count[char]>=freq:
                if count[char]==freq:
                    ans.append(char)
                else:
                    ans=[char]
                    freq=count[char]
        return ans

a=Solution()
print(a.mostCommonWord("jack and jill went to market to buy bread and cheese cheese is jack favorite food",["and","he","the","to","is"]))
print(a.mostCommonWord("   ",["and","he","the","to","is"]))
print(a.mostCommonWord("",["and","he","the","to","is"]))