
# 用两个dict分别记录checkin,checkout的人，以及每个路线的转换总时间+station个数(checkout时更新)

class UndergroundSystem:

    def __init__(self):
        self.check={}
        self.time={}

    def checkIn(self, id: int, stationName: str, t: int):
        self.check[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int):
        prevstation, prevt = self.check[id]
        time = t-prevt
        if (prevstation,stationName) in self.time:
            totaltime,stationN = self.time[(prevstation,stationName)]
            self.time[(prevstation,stationName)] = (totaltime+time,stationN+1)
        else:
            self.time[(prevstation,stationName)] = (time,1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime,stationN = self.time[(startStation,endStation)]
        return totaltime/stationN


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)