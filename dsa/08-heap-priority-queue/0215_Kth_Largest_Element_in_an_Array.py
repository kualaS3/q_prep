import heapq

class Solution:
    '''
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heap[0]
    ''' #apparently this is the expensive version, O(n + k log n) time

    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]          # copy of just the first k
        heapq.heapify(heap)      # O(k), turns those k into a valid min-heap
        for n in nums[k:]:       # stream the rest one at a time
            heapq.heappushpop(heap, n)
        return heap[0]
