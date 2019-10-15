
# 思路: 提取时间，放在tuple之前，根据时间和字符串大小进行排序

class Solution:
    def getEventsOrder(self,team1, team2, events1, events2):
        return [e[1] for e in sorted(self.parse(team1,events1)+self.parse(team2,events2))]

    def parse(self,team,events):
        ans=[]
        for e in events:
            e2,e3=e.split()[1],e.split()[2]
            t=None
            if e2.isdigit(): t=int(e2)
            elif '+' in e2: t=int(e2.split('+')[0])+int(e2.split('+')[1])/10
            elif e3.isdigit(): t=int(e3)
            else: t=int(e3.split('+')[0])+int(e3.split('+')[1])/10
            ans.append((t,team+" "+e))
        return ans

a=Solution()
print(a.getEventsOrder("EDC","CDE",["Name1 12 G", "FirstName LastName 43 Y"],["Name3 45+1 S SubName","Name4 46 G"]))