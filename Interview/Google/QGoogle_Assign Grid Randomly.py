
import random
class Random:

    def __init__(self, rows, cols, N_player):
        self.board = [[-1]*cols for _ in range(rows)]
        self.m = rows
        self.n = cols
        self.end = rows*cols-1
        self.i = 0
        self.N_player = N_player
        self.memo = {}

    def assign(self):
        x = random.randint(0, self.end)
        res = self.memo.get(x, x)
        self.memo[x] = self.memo.get(self.end, self.end)
        self.end-=1
        self.board[res//self.n][res%self.n] = self.i
        self.i = (self.i+1)%self.N_player

    def doit(self):
        for _ in range(self.m*self.n):
            self.assign()
        return self.board

    def doit2(self):
        limit = (self.m*self.n)/self.N_player
        player_count = [0]*self.N_player
        seeds = list(range(self.N_player))
        for i in range(self.m):
            for j in range(self.n):
                player = random.choice(seeds)
                self.board[i][j] = player
                player_count[player] += 1
                if player_count[player] == limit:
                    seeds.remove(player)
        return self.board


a=Random(4,4,4)
print(a.doit())
print(a.doit2())
