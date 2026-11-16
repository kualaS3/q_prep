import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap = [] 
        for i in range(k): 
            
            x,y = points[i]
            p = x**2 + y**2 # p is the size, * -1 for max heap
            heap.append((-p, [x, y]))

        heapq.heapify(heap)

        for n in points[k:]:
            x = n[0]
            y = n[1]
            heapq.heappushpop(heap, (-(x**2 + y**2), [x, y]))

        return [n for _, n in heap]
