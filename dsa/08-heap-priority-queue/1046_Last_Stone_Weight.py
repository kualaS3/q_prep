import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
            # can do 'heap = [-stone for stone in stones]'
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap, x-y)
        return -1 * heap[0]
