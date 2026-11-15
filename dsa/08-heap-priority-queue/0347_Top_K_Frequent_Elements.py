import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums :
            count[n] = count.get(n, 0) + 1 # remb get(x, n), n is the default num
        
        heap = []
        for c in count:
            heapq.heappush(heap, (count[c], c))
        while len(heap) > k:
            heapq.heappop(heap)
            
        return [num for freq, num in heap]
