class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        
        if len(stones)==1:
            return stones[0]
        
        for i in range(0, len(stones)):
            stones[i] = stones[i]*-1
        
        heap = stones
        heapq.heapify(stones)
        print(heap)
        while len(heap)>1:
            stone1 = -1* heap[0]
            heapq.heappop(heap)
            stone2 = -1* heap[0]
            heapq.heappop(heap)

            if stone1 == stone2 and len(heap)>0:
                continue
            elif stone1 == stone2 and len(heap)==0:
                
                newStone = (stone1-stone2)*-1

                heapq.heappush(heap, newStone)
            
            elif stone1>stone2:
                
                newStone = (stone1-stone2)*-1
                heapq.heappush(heap,newStone)
            else:
                
                newStone = (stone2-stone1)*-1
                heapq.heappush(heap,newStone)
        
        return heap[0]*-1

        

