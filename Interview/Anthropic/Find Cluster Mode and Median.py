from collections import Counter
class Worker:
    def __init__(self, workerId, k, localData, cluster):
        self.workerId = workerId
        self.k = k
        self.localData = localData
        self.cluster = cluster
        self.freq = {}

    def _calLocalWinner(self, golbalFreq):
        # Calculate local winner
        local_winner = float('-inf')
        max_f = -1
        for n, f in golbalFreq.items():
            if f > max_f:
                local_winner = n
                max_f = f
            elif f == max_f and n<local_winner:
                local_winner = n
        return local_winner, max_f

    def sendLocalFrequency(self):
        # Calculate frequency for each worker's local data
        for n in self.localData:
            self.freq[n] = self.freq.get(n,0) + 1
        for n, f in self.freq.items():
            # Send msg to %k's inbox
            self.sendAsyncMessage(n%self.k, f"DATA {n} {f}")
    
    def calGobalFrequency(self):
        golbalFreq = {}
        while True:
            data = self.receive()
            if not data: break
            parts = data.split(" ")
            n, f = int(parts[1]), int(parts[2])
            golbalFreq[n] = golbalFreq.get(n, 0) + f

        local_winner, max_f = self._calLocalWinner(golbalFreq)
        # Report local winner to worker 0
        if max_f>0: self.sendAsyncMessage(0, f"WINNER {local_winner} {max_f}")

    # Only for worker 0
    def calFinalWinner(self):
        final_winner = float('-inf')
        max_f = -1
        while True:
            data = self.receive()
            if not data: break
            parts = data.split(" ")
            local_winner, f = int(parts[1]), int(parts[2])
            if f > max_f: 
                final_winner = local_winner
                max_f = f
            elif f == max_f and local_winner < final_winner:
                final_winner = local_winner
        return final_winner if max_f>0 else None

    # Sends a string-represented payload data to the specified worker
    # asynchronously. You should NOT modify this method.
    def sendAsyncMessage(self, targetWorkerId, payload):
        self.cluster.sendAsyncMessage(targetWorkerId, payload)

    # Receives a string-represented payload data from the worker's mailbox. You
    # should NOT modify this method.
    def receive(self):
        return self.cluster.receive(self.workerId)

class Cluster:
    def __init__(self, data, k):
        self.k = k

        self.shards = []
        for i in range(k):
            self.shards.append([])

        # Distribute data evenly across workers
        totalSize = len(data)
        baseSize = totalSize // k
        remainder = totalSize % k

        index = 0
        for w in range(k):
            chunkSize = baseSize + (1 if w < remainder else 0)
            for j in range(chunkSize):
                self.shards[w].append(data[index])
                index += 1

        self.mailboxes = {}
        self.readIndices = {}
        for i in range(k):
            self.mailboxes[i] = []
            self.readIndices[i] = 0

        self.workers = [None] * k
        for i in range(k):
            self.workers[i] = Worker(i, k, self.shards[i], self)

    def sendAsyncMessage(self, targetWorkerId, payload):
        self.mailboxes[targetWorkerId].append(payload)

    def receive(self, workerId):
        myMailbox = self.mailboxes[workerId]
        idx = self.readIndices[workerId]
        if idx < len(myMailbox):
            self.readIndices[workerId] = idx + 1
            return myMailbox[idx]

        return ""

    def findMode(self):
        # every worker calculate local freq and send to %k worker
        for i in range(self.k):
            self.workers[i].sendLocalFrequency()
        
        # every worker calculate local winner and send to worker 0
        for i in range(self.k):
            self.workers[i].calGobalFrequency()
        
        # worker 0 calculate final winner
        return self.workers[0].calFinalWinner()

    @staticmethod
    def main():
        Cluster.test1()
        Cluster.test2()
        Cluster.test3()

    @staticmethod
    def test1():
        print("===== Test 1 =====")
        data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        cluster = Cluster(data, 3)
        print(cluster.findMode())  # Expected: 4

    @staticmethod
    def test2():
        print("===== Test 2 =====")
        data = [1, 2, 3, 1, 2, 3]
        cluster = Cluster(data, 2)
        print(cluster.findMode())  # Expected: 1

    @staticmethod
    def test3():
        print("===== Test 3 =====")
        data = []
        for i in range(1000):
            data.append(785)
        for i in range(999):
            data.append(3)
        for i in range(1001):
            data.append(1538)
        for i in range(20):
            data.append(5)
        cluster = Cluster(data, 10)
        print(cluster.findMode())  # Expected: 7


if __name__ == "__main__":
    Cluster.main()
