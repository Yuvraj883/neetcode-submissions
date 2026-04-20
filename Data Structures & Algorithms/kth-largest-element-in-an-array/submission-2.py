class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)
        
        heapq.heapify(heap)
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)