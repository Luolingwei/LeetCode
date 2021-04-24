import heapq
class Solution:

    def __init__(self):
        self.products = {}
        self.offers = {}
        self.offer2product = {}
        self.heaps = {}

    def add_offer(self, productId, offerId, price):
        if productId not in self.products:
            self.products[productId] = set()
            self.heaps[productId] = [[],[]]

        self.products[productId].add(offerId)
        self.offers[offerId] = price
        self.offer2product[offerId] = productId
        cur_heap = self.heaps[productId]
        heapq.heappush(cur_heap[1], price)
        if len(cur_heap[1]) > len(cur_heap[0]):
            heapq.heappush(cur_heap[0], -heapq.heappop(cur_heap[1]))

    def remove_offer(self, offerId):
        if offerId not in self.offers:
            return
        self.products[self.offer2product[offerId]].remove(offerId)
        self.offers.pop(offerId)
        self.offer2product.pop(offerId)

    def get_cloest_price(self, productId, target_price):
        if productId not in self.products:
            return
        # can use Java TreeSet to achieve O(logn) query
        offer_set = self.products[productId]
        res, min_dist = -1, float('inf')
        for offerId in offer_set:
            cur_price = self.offers[offerId]
            if abs(cur_price - target_price) < min_dist:
                min_dist = abs(cur_price - target_price)
                res = cur_price
        return res

    def get_median_price(self, productId):
        if productId not in self.products:
            return
        # can dynamically update heap in add_offer API
        maxH, minH = [], []
        N = len(self.products[productId])
        size = N//2 if N&1==0 else N//2+1
        for offerId in self.products[productId]:
            cur_price = self.offers[offerId]
            heapq.heappush(maxH, cur_price)
            if len(maxH) > size:
                heapq.heappop(maxH)
            heapq.heappush(minH, -cur_price)
            if len(minH) > size:
                heapq.heappop(minH)
        return (heapq.heappop(maxH) - heapq.heappop(minH)) // 2


a = Solution()
a.add_offer(1, 10, 100)
a.add_offer(1, 20, 200)
a.add_offer(1, 30, 300)
a.add_offer(1, 40, 400)
print(a.get_median_price(1))
print(a.get_cloest_price(1, 120))
print(a.get_cloest_price(1, 151))
a.remove_offer(10)
print(a.get_cloest_price(1, 120))
print(a.get_median_price(1))