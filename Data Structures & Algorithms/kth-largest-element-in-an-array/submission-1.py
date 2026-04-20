class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(-num)
            heap.append(-num)
        temp = []
        for num in uniqueNums: 
            temp.append(num)
        
        heapq.heapify(heap)
        print(heap)

        for i in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap) if heap else -1