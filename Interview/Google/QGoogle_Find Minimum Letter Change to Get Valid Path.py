import heapq
class Solution:

    def __init__(self):
        self.all_cities = ["AAA","BBB","CCC","DDD","EEE"]
        self.neighbors = {"AAA":["BBB","CCC"], "BBB":["CCC"], "CCC":["DDD"], "DDD":["EEE"], "EEE":["DDD"]}

    def list_all_city(self):
        return self.all_cities

    def get_neighbor(self, city):
        return self.neighbors[city]

    def find_change(self, trips):

        if not trips: return []

        q = []
        for start in self.list_all_city():
            q.append((self.cal_change(start, trips[0]), 0, start, [start]))

        while q:
            cur_change, pos, city, path = heapq.heappop(q)
            if pos == len(trips) - 1:
                return path
            for neighbor in self.get_neighbor(city):
                heapq.heappush(q, (cur_change + self.cal_change(trips[pos+1], neighbor), pos + 1, neighbor, path + [neighbor]))


    def cal_change(self, city1, city2):
        return sum(city1[i]!=city2[i] for i in range(len(city1)))


a=Solution()
print(a.find_change(["AAA","BBB","CCC","DDD","EEE"]))
print(a.find_change(["AAA","CCC","DDD","EEE"]))
print(a.find_change(["AAA","CCC","EEE","DDD"]))
print(a.find_change(["AAA","CCC","EDE","DDD"]))
print(a.find_change(["AAA","CCC","XXX","XXX"]))
print(a.find_change(["AAA","CCC","EDE","DDD","EEE","FFF"]))