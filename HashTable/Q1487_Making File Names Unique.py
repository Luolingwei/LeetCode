from collections import defaultdict

# memo records the number of a certain symbol we already have, so when we come across a symbol in memo's keys,
# we append [name(str(memo[name]))], and set [name(str(memo[name]))]'s number to 1 (it's new to memo)
# one thing to note is that name(str(memo[name])) may already exist because of directly add symbol like "name(3)"
# so we add a while loop to deal with it, everytime we need to increase the number of name itself.

class Solution:
    def getFolderNames(self, names):
        memo = defaultdict(int)
        res = []
        for n in names:
            if memo[n] > 0:
                while n+'('+ str(memo[n]) +')' in memo.keys():
                    memo[n]+=1
                res.append(n+'('+ str(memo[n]) +')')
                memo[n+'('+ str(memo[n])+')']+=1
            else:
                res.append(n)
            memo[n]+=1
        return res


a=Solution()
print(a.getFolderNames(["pes","fifa","gta","pes(2019)"]))
print(a.getFolderNames(["gta","gta(1)","gta","avalon"]))
print(a.getFolderNames(["wano","wano","wano","wano"]))
print(a.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
print(a.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))